import random
import math

import utils
from system import System
from star_map import StarMap
from terrain import Terrain, TERRAIN_NAMES


def generate_random_clusters_starmap(
        num_players=7, systems=350, galaxy_radius=30, terrain_radius=10, terrain_size=25, terrain_delta=3,
        terrains_connections=2, connected_systems=2
):
    description = (
        f"{num_players=}, {systems=}, {galaxy_radius=}, {terrain_radius=}, {terrain_size=}, "
        f"{terrain_delta=}, {terrains_connections=}, {connected_systems=}"
    )
    star_map = StarMap(num_players, f"Random clusters {random.randint(1000, 9999)}", description)

    # stars per terrain
    star_chunks = [x for x in utils.random_chunks(list(range(systems)), terrain_size, terrain_delta)]

    # each chunk - new terrain, with amount of stars equal to chunk size
    system_guid = 1000
    for chunk in star_chunks:
        terrain_coords = utils.random_point_in_sphere(0, 0, 0, galaxy_radius)
        terrain = Terrain(star_map.features, *terrain_coords, random.choice(TERRAIN_NAMES))

        for _ in chunk:
            system_guid += 1
            system = System(
                terrain_features=terrain.terrain_features,
                system_guid=system_guid,
                terrain_coordinates=(0, 0, 0, terrain_radius),
            )
            terrain.systems.append(system)

        terrain.generate_node_lines()
        star_map.terrains.append(terrain)

    starting_terrains = random.sample(star_map.terrains, num_players)
    for index, starting_terrain in enumerate(starting_terrains):
        starting_system = random.choice(starting_terrain.systems)
        starting_system.make_starting_system(index + 1)

    star_map.generate_cross_terrains_node_lines(terrains_connections, connected_systems)
    star_map.save_map(debug=False)


def generate_random_sphere_starmap(
        num_players=7, systems=350, galaxy_radius=25, terrain_size=25,
        terrains_connections=3, connected_systems=4
):
    star_map = StarMap(
        num_players,
        f"Random sphere {random.randint(1000, 9999)}",
        (f"Random sphere {num_players=}, {systems=}, {galaxy_radius=}, {terrain_size=} "
         f"{terrains_connections=} {connected_systems=}")
    )

    # temporary terrain to generate star systems around the star map center
    temporary_terrain = Terrain(star_map.features, 0, 0, 0, random.choice(TERRAIN_NAMES))

    # generate star systems
    system_guid = 1000
    for _ in range(systems):
        system_guid += 1
        system = System(
            terrain_features=temporary_terrain.terrain_features,
            system_guid=system_guid,
            terrain_coordinates=(*temporary_terrain.coordinates, galaxy_radius),
        )
        temporary_terrain.systems.append(system)

    # generate terrains, atleast 1 terrain per player
    terrains_needed = max([num_players, math.ceil(systems / terrain_size)])
    terrain_names = random.sample(TERRAIN_NAMES, terrains_needed)
    terrains = []

    for terrain in range(terrains_needed):
        terrain_system = temporary_terrain.systems.pop()
        terrain = Terrain(star_map.features, *terrain_system.coordinates, terrain_names.pop())
        terrain_system.update_system_coordinates(
            x=terrain_system.coordinates[0] - terrain.coordinates[0],
            y=terrain_system.coordinates[1] - terrain.coordinates[1],
            z=terrain_system.coordinates[2] - terrain.coordinates[2],
        )
        terrain_system.move_to_another_terrain(terrain)
        terrain.systems.append(terrain_system)
        terrains.append(terrain)
        star_map.terrains.append(terrain)

    # move systems from temporary terrain to closest
    # this approache is not perfect, and some systems may be far aways from it best terrain, if it has enough stars
    for system in temporary_terrain.systems:
        terrains.sort(key=lambda x: utils.distance(*system.coordinates, *x.coordinates))
        for terrain in terrains:
            if len(terrain.systems) < terrain_size:
                system.move_to_another_terrain(terrain)
                # Coordinates in LocalSpace is relative to the terrain, but to make sphere, not clusters
                # we need posistion system relative to the map center, as it was initially done using
                # temporary terrain with 0, 0, 0 coordinates
                system.update_system_coordinates(
                    x=system.coordinates[0] - terrain.coordinates[0],
                    y=system.coordinates[1] - terrain.coordinates[1],
                    z=system.coordinates[2] - terrain.coordinates[2],
                )
                terrain.systems.append(system)
                break

    # choose starting systems
    for player, terrain in enumerate(random.sample(terrains, num_players)):
        system = random.choice(terrain.systems)
        system.make_starting_system(player + 1)

    # generate nodes
    for terrain in terrains:
        terrain.generate_node_lines()

    # delete temporary terrain
    star_map.features.remove(temporary_terrain.terrain)

    star_map.generate_cross_terrains_node_lines(terrains_connections, connected_systems)
    star_map.save_map(debug=False)
