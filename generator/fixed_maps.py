import random

from terrain import Terrain, TERRAIN_NAMES
from star_map import StarMap
from system import System


def cake_for_8():
    players = 8

    star_map = StarMap(players, "Cake", "Cake for 8 hungry aliens")

    # 1st terrain
    terrain_names = random.sample(TERRAIN_NAMES, players)
    terrain = Terrain(star_map.features, 5, 0, 0, terrain_names.pop())

    # 1st layer
    system_1 = System(terrain.terrain_features, 1, fixed_coordinates=(10, 0, 0))
    system_2 = System(terrain.terrain_features, 2, fixed_coordinates=(20, 6, 0))
    system_3 = System(terrain.terrain_features, 3, fixed_coordinates=(20, -6, 0))
    system_4 = System(terrain.terrain_features, 4, fixed_coordinates=(30, 0, 0))
    system_5 = System(terrain.terrain_features, 5, fixed_coordinates=(30, 12, 0))
    system_6 = System(terrain.terrain_features, 6, fixed_coordinates=(30, -12, 0))
    system_7 = System(terrain.terrain_features, 7, fixed_coordinates=(40, 6, 0))
    system_8 = System(terrain.terrain_features, 8, fixed_coordinates=(40, -6, 0))
    system_9 = System(terrain.terrain_features, 9, fixed_coordinates=(40, 18, 0))
    system_10 = System(terrain.terrain_features, 10, fixed_coordinates=(40, -18, 0))

    # 2nd layyer
    system_11 = System(terrain.terrain_features, 11, fixed_coordinates=(10, 0, 10))
    system_12 = System(terrain.terrain_features, 12, fixed_coordinates=(20, 6, 10))
    system_13 = System(terrain.terrain_features, 13, fixed_coordinates=(20, -6, 10))
    system_14 = System(terrain.terrain_features, 14, fixed_coordinates=(30, 0, 10))
    system_15 = System(terrain.terrain_features, 15, fixed_coordinates=(30, 12, 10))
    system_16 = System(terrain.terrain_features, 16, fixed_coordinates=(30, -12, 10))
    system_17 = System(terrain.terrain_features, 17, fixed_coordinates=(40, 6, 10))
    system_18 = System(terrain.terrain_features, 18, fixed_coordinates=(40, -6, 10))
    system_19 = System(terrain.terrain_features, 19, fixed_coordinates=(40, 18, 10))
    system_20 = System(terrain.terrain_features, 20, fixed_coordinates=(40, -18, 10))

    # 3rd layer
    system_21 = System(terrain.terrain_features, 21, fixed_coordinates=(10, 0, 20))
    system_22 = System(terrain.terrain_features, 22, fixed_coordinates=(20, 6, 20))
    system_23 = System(terrain.terrain_features, 23, fixed_coordinates=(20, -6, 20))
    system_24 = System(terrain.terrain_features, 24, fixed_coordinates=(30, 0, 20))
    system_25 = System(terrain.terrain_features, 25, fixed_coordinates=(30, 12, 20))
    system_26 = System(terrain.terrain_features, 26, fixed_coordinates=(30, -12, 20))
    system_27 = System(terrain.terrain_features, 27, fixed_coordinates=(40, 6, 20))
    system_28 = System(terrain.terrain_features, 28, fixed_coordinates=(40, -6, 20))
    system_29 = System(terrain.terrain_features, 29, fixed_coordinates=(40, 18, 20))
    system_30 = System(terrain.terrain_features, 30, fixed_coordinates=(40, -18, 20))

    system_2.make_starting_system(1)
    system_28.make_starting_system(2)
    terrain.systems.extend([
        system_1, system_2, system_3, system_4, system_5, system_6, system_7, system_8, system_9, system_10,
        system_11, system_12, system_13, system_14, system_15, system_16, system_17, system_18, system_19, system_20,
        system_21, system_22, system_23, system_24, system_25, system_26, system_27, system_28, system_29, system_30,
    ])
    terrain.generate_node_lines()

    # 2nd terrain
    terrain_names = random.sample(TERRAIN_NAMES, players)
    terrain2 = Terrain(star_map.features, -5, 0, 0, terrain_names.pop())

    # 1st layer
    system_31 = System(terrain2.terrain_features, 31, fixed_coordinates=(-10, 0, 0))
    system_32 = System(terrain2.terrain_features, 32, fixed_coordinates=(-20, 6, 0))
    system_33 = System(terrain2.terrain_features, 33, fixed_coordinates=(-20, -6, 0))
    system_34 = System(terrain2.terrain_features, 34, fixed_coordinates=(-30, 0, 0))
    system_35 = System(terrain2.terrain_features, 35, fixed_coordinates=(-30, 12, 0))
    system_36 = System(terrain2.terrain_features, 36, fixed_coordinates=(-30, -12, 0))
    system_37 = System(terrain2.terrain_features, 37, fixed_coordinates=(-40, 6, 0))
    system_38 = System(terrain2.terrain_features, 38, fixed_coordinates=(-40, -6, 0))
    system_39 = System(terrain2.terrain_features, 39, fixed_coordinates=(-40, 18, 0))
    system_40 = System(terrain2.terrain_features, 40, fixed_coordinates=(-40, -18, 0))

    # 2nd layyer
    system_41 = System(terrain2.terrain_features, 41, fixed_coordinates=(-10, 0, 10))
    system_42 = System(terrain2.terrain_features, 42, fixed_coordinates=(-20, 6, 10))
    system_43 = System(terrain2.terrain_features, 43, fixed_coordinates=(-20, -6, 10))
    system_44 = System(terrain2.terrain_features, 44, fixed_coordinates=(-30, 0, 10))
    system_45 = System(terrain2.terrain_features, 45, fixed_coordinates=(-30, 12, 10))
    system_46 = System(terrain2.terrain_features, 46, fixed_coordinates=(-30, -12, 10))
    system_47 = System(terrain2.terrain_features, 47, fixed_coordinates=(-40, 6, 10))
    system_48 = System(terrain2.terrain_features, 48, fixed_coordinates=(-40, -6, 10))
    system_49 = System(terrain2.terrain_features, 49, fixed_coordinates=(-40, 18, 10))
    system_50 = System(terrain2.terrain_features, 50, fixed_coordinates=(-40, -18, 10))

    # 3rd layer
    system_51 = System(terrain2.terrain_features, 51, fixed_coordinates=(-10, 0, 20))
    system_52 = System(terrain2.terrain_features, 52, fixed_coordinates=(-20, 6, 20))
    system_53 = System(terrain2.terrain_features, 53, fixed_coordinates=(-20, -6, 20))
    system_54 = System(terrain2.terrain_features, 54, fixed_coordinates=(-30, 0, 20))
    system_55 = System(terrain2.terrain_features, 55, fixed_coordinates=(-30, 12, 20))
    system_56 = System(terrain2.terrain_features, 56, fixed_coordinates=(-30, -12, 20))
    system_57 = System(terrain2.terrain_features, 57, fixed_coordinates=(-40, 6, 20))
    system_58 = System(terrain2.terrain_features, 58, fixed_coordinates=(-40, -6, 20))
    system_59 = System(terrain2.terrain_features, 59, fixed_coordinates=(-40, 18, 20))
    system_60 = System(terrain2.terrain_features, 60, fixed_coordinates=(-40, -18, 20))

    system_32.make_starting_system(3)
    system_58.make_starting_system(4)
    terrain2.systems.extend([
        system_31, system_32, system_33, system_34, system_35, system_36, system_37, system_38, system_39, system_40,
        system_41, system_42, system_43, system_44, system_45, system_46, system_47, system_48, system_49, system_50,
        system_51, system_52, system_53, system_54, system_55, system_56, system_57, system_58, system_59, system_60,
    ])
    terrain2.generate_node_lines()

    # 3rd terrain
    terrain_names = random.sample(TERRAIN_NAMES, players)
    terrain3 = Terrain(star_map.features, 0, -5, 0, terrain_names.pop())

    # 1st layer
    system_61 = System(terrain3.terrain_features, 61, fixed_coordinates=(0, -10, 0))
    system_62 = System(terrain3.terrain_features, 62, fixed_coordinates=(6, -20, 0))
    system_63 = System(terrain3.terrain_features, 63, fixed_coordinates=(-6, -20, 0))
    system_64 = System(terrain3.terrain_features, 64, fixed_coordinates=(0, -30, 0))
    system_65 = System(terrain3.terrain_features, 65, fixed_coordinates=(12, -30, 0))
    system_66 = System(terrain3.terrain_features, 66, fixed_coordinates=(-12, -30, 0))
    system_67 = System(terrain3.terrain_features, 67, fixed_coordinates=(6, -40, 0))
    system_68 = System(terrain3.terrain_features, 68, fixed_coordinates=(-6, -40, 0))
    system_69 = System(terrain3.terrain_features, 69, fixed_coordinates=(18, -40, 0))
    system_70 = System(terrain3.terrain_features, 70, fixed_coordinates=(-18, -40, 0))

    # 2nd layyer
    system_71 = System(terrain3.terrain_features, 71, fixed_coordinates=(0, -10, 10))
    system_72 = System(terrain3.terrain_features, 72, fixed_coordinates=(6, -20, 10))
    system_73 = System(terrain3.terrain_features, 73, fixed_coordinates=(-6, -20, 10))
    system_74 = System(terrain3.terrain_features, 74, fixed_coordinates=(0, -30, 10))
    system_75 = System(terrain3.terrain_features, 75, fixed_coordinates=(12, -30, 10))
    system_76 = System(terrain3.terrain_features, 76, fixed_coordinates=(-12, -30, 10))
    system_77 = System(terrain3.terrain_features, 77, fixed_coordinates=(6, -40, 10))
    system_78 = System(terrain3.terrain_features, 78, fixed_coordinates=(-6, -40, 10))
    system_79 = System(terrain3.terrain_features, 79, fixed_coordinates=(18, -40, 10))
    system_80 = System(terrain3.terrain_features, 80, fixed_coordinates=(-18, -40, 10))

    # 3rd layer
    system_81 = System(terrain3.terrain_features, 81, fixed_coordinates=(0, -10, 20))
    system_82 = System(terrain3.terrain_features, 82, fixed_coordinates=(6, -20, 20))
    system_83 = System(terrain3.terrain_features, 83, fixed_coordinates=(-6, -20, 20))
    system_84 = System(terrain3.terrain_features, 84, fixed_coordinates=(0, -30, 20))
    system_85 = System(terrain3.terrain_features, 85, fixed_coordinates=(12, -30, 20))
    system_86 = System(terrain3.terrain_features, 86, fixed_coordinates=(-12, -30, 20))
    system_87 = System(terrain3.terrain_features, 87, fixed_coordinates=(6, -40, 20))
    system_88 = System(terrain3.terrain_features, 88, fixed_coordinates=(-6, -40, 20))
    system_89 = System(terrain3.terrain_features, 89, fixed_coordinates=(18, -40, 20))
    system_90 = System(terrain3.terrain_features, 90, fixed_coordinates=(-18, -40, 20))

    system_62.make_starting_system(5)
    system_88.make_starting_system(6)
    terrain3.systems.extend([
        system_61, system_62, system_63, system_64, system_65, system_66, system_67, system_68, system_69, system_70,
        system_71, system_72, system_73, system_74, system_75, system_76, system_77, system_78, system_79, system_80,
        system_81, system_82, system_83, system_84, system_85, system_86, system_87, system_88, system_89, system_90,
    ])
    terrain3.generate_node_lines()

    # 4th terrain
    terrain_names = random.sample(TERRAIN_NAMES, players)
    terrain4 = Terrain(star_map.features, 0, 5, 0, terrain_names.pop())

    # 1st layer
    system_91 = System(terrain4.terrain_features, 91, fixed_coordinates=(0, 10, 0))
    system_92 = System(terrain4.terrain_features, 92, fixed_coordinates=(6, 20, 0))
    system_93 = System(terrain4.terrain_features, 93, fixed_coordinates=(-6, 20, 0))
    system_94 = System(terrain4.terrain_features, 94, fixed_coordinates=(0, 30, 0))
    system_95 = System(terrain4.terrain_features, 95, fixed_coordinates=(12, 30, 0))
    system_96 = System(terrain4.terrain_features, 96, fixed_coordinates=(-12, 30, 0))
    system_97 = System(terrain4.terrain_features, 97, fixed_coordinates=(6, 40, 0))
    system_98 = System(terrain4.terrain_features, 98, fixed_coordinates=(-6, 40, 0))
    system_99 = System(terrain4.terrain_features, 99, fixed_coordinates=(18, 40, 0))
    system_100 = System(terrain4.terrain_features, 100, fixed_coordinates=(-18, 40, 0))

    # 2nd layyer
    system_101 = System(terrain4.terrain_features, 101, fixed_coordinates=(0, 10, 10))
    system_102 = System(terrain4.terrain_features, 102, fixed_coordinates=(6, 20, 10))
    system_103 = System(terrain4.terrain_features, 103, fixed_coordinates=(-6, 20, 10))
    system_104 = System(terrain4.terrain_features, 104, fixed_coordinates=(0, 30, 10))
    system_105 = System(terrain4.terrain_features, 105, fixed_coordinates=(12, 30, 10))
    system_106 = System(terrain4.terrain_features, 106, fixed_coordinates=(-12, 30, 10))
    system_107 = System(terrain4.terrain_features, 107, fixed_coordinates=(6, 40, 10))
    system_108 = System(terrain4.terrain_features, 108, fixed_coordinates=(-6, 40, 10))
    system_109 = System(terrain4.terrain_features, 109, fixed_coordinates=(18, 40, 10))
    system_110 = System(terrain4.terrain_features, 110, fixed_coordinates=(-18, 40, 10))

    # 3rd layer
    system_111 = System(terrain4.terrain_features, 111, fixed_coordinates=(0, 10, 20))
    system_112 = System(terrain4.terrain_features, 112, fixed_coordinates=(6, 20, 20))
    system_113 = System(terrain4.terrain_features, 113, fixed_coordinates=(-6, 20, 20))
    system_114 = System(terrain4.terrain_features, 114, fixed_coordinates=(0, 30, 20))
    system_115 = System(terrain4.terrain_features, 115, fixed_coordinates=(12, 30, 20))
    system_116 = System(terrain4.terrain_features, 116, fixed_coordinates=(-12, 30, 20))
    system_117 = System(terrain4.terrain_features, 117, fixed_coordinates=(6, 40, 20))
    system_118 = System(terrain4.terrain_features, 118, fixed_coordinates=(-6, 40, 20))
    system_119 = System(terrain4.terrain_features, 119, fixed_coordinates=(18, 40, 20))
    system_120 = System(terrain4.terrain_features, 120, fixed_coordinates=(-18, 40, 20))

    system_92.make_starting_system(7)
    system_118.make_starting_system(8)
    terrain4.systems.extend([
        system_91, system_92, system_93, system_94, system_95, system_96, system_97, system_98, system_99, system_100,
        system_101, system_102, system_103, system_104, system_105, system_106, system_107, system_108, system_109, system_110,
        system_111, system_112, system_113, system_114, system_115, system_116, system_117, system_118, system_119, system_120,
    ])
    terrain4.generate_node_lines()

    star_map.terrains.extend([terrain, terrain2, terrain3, terrain4])
    star_map.generate_cross_terrains_node_lines()
    star_map.save_map()

cake_for_8()
