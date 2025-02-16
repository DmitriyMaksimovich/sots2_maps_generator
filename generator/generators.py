import random

from system import System
from star_map import StarMap
from terrain import Terrain, TERRAIN_NAMES


def generate_random_sphere_starmap(num_players=6, systems=300):
    star_map = StarMap(num_players, "Random sphere", "Random sphere")
    terrain = Terrain(star_map.features, 0, 0, 0, random.choice(TERRAIN_NAMES))

    system_guid = 1000
    for _ in range(systems):
        system_guid += 1
        system = System(
            terrain_features=terrain.terrain_features,
            system_guid=system_guid,
            terrain_coordinates=(0, 0, 0, 70),
        )
        terrain.systems.append(system)

    starting_systems = random.sample(terrain.systems, num_players)
    for player, system in enumerate(starting_systems):
        system.make_starting_system(player + 1)

    terrain.generate_node_lines()
    star_map.save_map(debug=True)


if __name__ == "__main__":
    generate_random_sphere_starmap()
