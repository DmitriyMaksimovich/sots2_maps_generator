import random
import math

import utils
from system import System
from star_map import StarMap
from terrain import Terrain, TERRAIN_NAMES


def generate_random_clusters_starmap(num_players=7, systems=350, galaxy_radius=20):
    random_index = random.randint(1000, 9999)
    system_guid = 1000

    star_map = StarMap(num_players, f"Random clusters {random_index}", "Random clusters")

    # stars per terrain
    star_chunks = [x for x in utils.random_chunks(list(range(systems)), 25, 3)]

    # each chunk - new terrain, with amount of stars equal to chunk size
    for chunk in star_chunks:
        terrain_coords = utils.random_point_in_sphere(0, 0, 0, galaxy_radius)
        terrain = Terrain(star_map.features, *terrain_coords, random.choice(TERRAIN_NAMES))

        for _ in chunk:
            system_guid += 1
            system = System(
                terrain_features=terrain.terrain_features,
                system_guid=system_guid,
                terrain_coordinates=(*terrain_coords, 9),
            )
            terrain.systems.append(system)

        terrain.generate_node_lines()
        star_map.terrains.append(terrain)

    starting_terrains = random.sample(star_map.terrains, num_players)
    for index, starting_terrain in enumerate(starting_terrains):
        starting_system = random.choice(starting_terrain.systems)
        starting_system.make_starting_system(index + 1)

    star_map.save_map(debug=False)


def generate_random_sphere_starmap(num_players=7, systems=650, galaxy_radius=20):
    random_index = random.randint(1000, 9999)
    system_guid = 1000
    terrain_avarage_size = 25

    star_map = StarMap(num_players, f"Random sphere {random_index}", "Random sphere")

    # temporary terrain to generate star systems around the star map center
    temporary_terrain = Terrain(star_map.features, 0, 0, 0, random.choice(TERRAIN_NAMES))

    # generate star systems
    for _ in range(systems):
        system_guid += 1
        system = System(
            terrain_features=temporary_terrain.terrain_features,
            system_guid=system_guid,
            terrain_coordinates=(*temporary_terrain.coordinates, galaxy_radius),
        )
        temporary_terrain.systems.append(system)

    # choose random systems as start positions; create a terrain for each
    terrains = []
    for player in range(num_players):
        starting_system = temporary_terrain.systems.pop()
        starting_system.make_starting_system(player + 1)
        terrain = Terrain(star_map.features, *starting_system.coordinates, random.choice(TERRAIN_NAMES))
        terrains.append(terrain)
        starting_system.move_to_another_terrain(terrain)

    # add more terrains using random systems as starting point
    extra_terrains_needed = math.ceil(systems / terrain_avarage_size) - len(terrains)

    for terrain in range(extra_terrains_needed):
        terrain_system = temporary_terrain.systems.pop()
        terrain = Terrain(star_map.features, *terrain_system.coordinates, random.choice(TERRAIN_NAMES))
        terrain_system.move_to_another_terrain(terrain)
        terrain.systems.append(terrain_system)
        terrains.append(terrain)

    # move systems from temporary terrain to closest
    for system in temporary_terrain.systems:
        terrains.sort(key=lambda x: utils.distance(*system.coordinates, *x.coordinates))
        for terrain in terrains:
            if len(terrain.systems) < terrain_avarage_size:
                system.move_to_another_terrain(terrain)
                terrain.systems.append(system)
                break

    # generate nodes, save
    for terrain in terrains:
        terrain.generate_node_lines()

    # delete temporary terrain
    star_map.features.remove(temporary_terrain.terrain)
    star_map.save_map(debug=False)


if __name__ == "__main__":
    # generate_random_clusters_starmap()
    generate_random_sphere_starmap()
