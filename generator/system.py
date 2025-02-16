import random
import math
import xml.etree.ElementTree as ET
from xml.dom.minidom import Element
from typing import Optional, List

from node_line import NodeLine


class System(Element):
    def __init__(
        self,
        terrain_features: ET.Element,
        system_guid: int,
        *,
        terrain_coordinates: Optional[tuple[float, float, float, float]] = None,
        fixed_coordinates: Optional[tuple[float, float, float]] = None,
        player_slot: int = 1,
        is_start_location: bool = False,
        system_name: Optional[str] = None
    ):
        """
        terrain_features: parent xml node; cluster of stars
        terrain_coordinates[x, y, z, max_distance_from_center]:
            terain center coordinates and max distance from it for randon generated system position
        fixed_coordinates[x, y, z]
        system_guid: uniq id of the system
        player_slot: player (person or ai index), requred if is_start_location == True
        is_start_location: is this system home system for player or ai
        system_name: system name
        """
        self.system = ET.SubElement(terrain_features, "System")
        self.system_guid = system_guid
        self.terrain_features = terrain_features

        self.node_lines_num = 0
        self.node_lines: List[NodeLine] = []

        if terrain_coordinates:
            x, y, z = self.random_point_in_sphere(*terrain_coordinates)
        elif fixed_coordinates:
            x, y, z = fixed_coordinates
        else:
            raise ValueError("terrain_coordinates or fixed_coordinates required")

        ET.SubElement(self.system, "Name").text = system_name if system_name else "Random System"
        ET.SubElement(self.system, "LocalSpace").text = f"0.1,0,0,0,0,0.1,0,0,0,0,0.1,0,{x},{y},{z},1"
        ET.SubElement(self.system, "IsVisible").text = "True"
        ET.SubElement(self.system, "ProvinceId")
        ET.SubElement(self.system, "Guid").text = str(system_guid)
        ET.SubElement(self.system, "Randomize").text = "True"
        ET.SubElement(self.system, "Type")
        ET.SubElement(self.system, "SubType")
        ET.SubElement(self.system, "Size")
        ET.SubElement(self.system, "Orbits")

        if is_start_location:
            ET.SubElement(self.system, "PlayerSlot").text = str(player_slot)
            ET.SubElement(self.system, "IsStartLocation").text = "True"
        else:
            ET.SubElement(self.system, "IsStartLocation").text = "False"

    def make_starting_system(self, player_slot: int):
        ET.SubElement(self.system, "PlayerSlot").text = str(player_slot)
        self.system.find("IsStartLocation").text = "True"

    def move_to_another_terrain(self, new_terrain):
        self.terrain_features.remove(self.system)
        new_terrain.terrain_features.append(self.system)
        self.terrain_features = new_terrain.terrain_features

    def random_point_in_sphere(self, center_x, center_y, center_z, radius):
        r = radius * (random.uniform(0, 1) ** (1/3))

        # Generate a random direction using spherical coordinates
        theta = random.uniform(0, 2 * math.pi)  # Random angle around Z-axis
        phi = math.acos(random.uniform(-1, 1))  # Random angle from Z-axis

        # Convert spherical coordinates to Cartesian
        x = center_x + r * math.sin(phi) * math.cos(theta)
        y = center_y + r * math.sin(phi) * math.sin(theta)
        z = center_z + r * math.cos(phi)

        return x, y, z
