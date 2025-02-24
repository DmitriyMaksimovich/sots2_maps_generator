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
        self.node_lines_et = ET.SubElement(self.root, "NodeLines")
        ET.SubElement(self.root, "Title").text = self.map_name
        ET.SubElement(self.root, "Description").text = map_description
        ET.SubElement(self.root, "NumPlayers").text = str(players_num)
        ET.SubElement(self.root, "PreviewTexture")
        ET.SubElement(self.root, "Provinces")
        self.terrains: List[Terrain] = []
        self.node_lines: List[NodeLine] = []

    def save_map(self, debug=False):
        tree = ET.ElementTree(self.root)
        file_name = self.map_name.replace(" ", "_")
        if debug:
            tree.write(f"DEBUG {file_name}.Starmap")
            xmlstr = minidom.parseString(ET.tostring(self.root)).toprettyxml(indent="   ")
            with open(f"{file_name}.xml", "w") as f:
                f.write(xmlstr)
        else:
            tree.write(f"{file_name}.Starmap")

    def generate_cross_terrains_node_lines(self, terrains_connections=2, connected_systems=2):
        """
        connect terrains with $terrains_connections closest terrains
        by creating node lines between $connected_systems systems
        """
        _terrains = []
        while self.terrains:
            terrain = self.terrains.pop()
            _terrains.append(terrain)
            self.terrains.sort(key=lambda x: utils.distance(*terrain.coordinates, *x.coordinates))
            for _terrain_to_connect in self.terrains:
                if len(terrain.connected_terrains) == terrains_connections:
                    # enough terrains connected
                    break
                if len(_terrain_to_connect.connected_terrains) == terrains_connections:
                    # target terrain has enough connection and can't be connected one more time
                    continue

                terrain.systems.sort(
                    key=lambda x: utils.distance(
                        *_terrain_to_connect.coordinates,
                        *utils.system_in_terrain_coordinates_to_global_coordinates(x, terrain)
                    )
                )
                _terrain_to_connect.systems.sort(
                    key=lambda x: utils.distance(
                        *terrain.coordinates,
                        *utils.system_in_terrain_coordinates_to_global_coordinates(x, _terrain_to_connect)
                    )
                )
                for index in range(connected_systems):
                    node_line = NodeLine(
                        self.node_lines_et,
                        terrain.systems[index].system_guid,
                        _terrain_to_connect.systems[index].system_guid,
                    )
                    self.node_lines.append(node_line)
                if _terrain_to_connect not in terrain.connected_terrains:
                    terrain.connected_terrains.append(_terrain_to_connect)
                    _terrain_to_connect.connected_terrains.append(terrain)

        self.terrains = _terrains
