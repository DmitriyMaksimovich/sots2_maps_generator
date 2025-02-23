import random
from typing import List
from xml.dom import minidom
from xml.dom.minidom import Element

import xml.etree.ElementTree as ET

import utils
from node_line import NodeLine
from terrain import Terrain


class StarMap(Element):
    def __init__(
        self,
        players_num: int,
        title: str,
        description: str = "",
    ):
        """
        players_num: players num
        title: map name
        description: map description
        """
        self.root = ET.Element("Starmap")
        self.players_num = players_num
        self.map_name = title if title else f"Random map {random.randint(1, 999999)}"
        map_description = description if description else "Random map"
        self.features = ET.SubElement(self.root, "Features")
        self.node_lines = ET.SubElement(self.root, "NodeLines")
        ET.SubElement(self.root, "Title").text = self.map_name
        ET.SubElement(self.root, "Description").text = map_description
        ET.SubElement(self.root, "NumPlayers").text = str(players_num)
        ET.SubElement(self.root, "PreviewTexture")
        ET.SubElement(self.root, "Provinces")
        self.terrains: List[Terrain] = []

    def save_map(self, debug=False):
        tree = ET.ElementTree(self.root)
        file_name = self.map_name.replace(" ", "_")
        tree.write(f"{file_name}.Starmap")

        if debug:
            xmlstr = minidom.parseString(ET.tostring(self.root)).toprettyxml(indent="   ")
            with open(f"{file_name}.xml", "w") as f:
                f.write(xmlstr)

    def generate_cross_terrains_node_lines(self, terrains_connections=2, connected_systems=2):
        # connect with two closest terrains
        _terrains = []
        while self.terrains:
            terrain = self.terrains.pop()
            _terrains.append(terrain)
            self.terrains.sort(key=lambda x: utils.distance(*terrain.coordinates, *x.coordinates))
            for _terrain_to_connect in self.terrains:
                if len(terrain.connected_terrains) == terrains_connections:
                    break
                if len(_terrain_to_connect.connected_terrains) == terrains_connections:
                    continue
                # TODO choose 2 closest systems
                for _ in range(connected_systems):
                    node_line = NodeLine(
                        self.node_lines,
                        random.choice(terrain.systems).system_guid,
                        random.choice(_terrain_to_connect.systems).system_guid,
                    )
                    terrain.connected_terrains.append(_terrain_to_connect)
                    _terrain_to_connect.connected_terrains.append(terrain)

        self.terrains = _terrains
