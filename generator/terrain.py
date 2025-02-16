import random
import xml.etree.ElementTree as ET
from xml.dom.minidom import Element
from typing import List

from system import System
from node_line import NodeLine

NODE_LINES_PER_SYSTEM_WEIGHTS = {
    1: 2,
    2: 8,
    3: 6,
    4: 2,
    5: 1,
}

class Terrain(Element):
    def __init__(
        self,
        features: ET.Element,
        terrain_x: float,
        terrain_y: float,
        terrain_z: float,
        terrain_name: str,
    ):
        """
        features: parent xml node
        terrain_x, terrain_y, terran_z: terain center coordinates
        terrain_name: terrain name
        """
        self.terrain = ET.SubElement(features, "Terrain")
        ET.SubElement(self.terrain, "Name").text = terrain_name
        ET.SubElement(self.terrain, "LocalSpace").text = f"1,0,0,0,0,1,0,0,0,0,1,0,{terrain_x},{terrain_y},{terrain_z},1"
        ET.SubElement(self.terrain, "Inherit").text = terrain_name
        ET.SubElement(self.terrain, "IsVisible").text = "True"
        ET.SubElement(self.terrain, "Provinces")

        self.terrain_features = ET.SubElement(self.terrain, "Features")
        self.systems: List[System] = []
        self.node_lines = ET.SubElement(self.terrain, "NodeLines")

    def generate_node_lines(self, weights=NODE_LINES_PER_SYSTEM_WEIGHTS):
        self.terrain.remove(self.node_lines)
        self.node_lines = ET.SubElement(self.terrain, "NodeLines")

        _nodes = []
        _weights = []
        for nodes, weight in  weights.items():
            _nodes.append(nodes)
            _weights.append(weight)

        for system in self.systems:
            system.node_lines_num = random.choices(_nodes, weights=_weights, k=1)[0]

        for system_a in self.systems:
            if system_a.node_lines_num != len(system_a.node_lines):

                for system_b in self.systems:
                    if system_b.node_lines_num != len(system_b.node_lines) and system_a != system_b:
                        node_line = NodeLine(self.node_lines, system_a.system_guid, system_b.system_guid)
                        system_a.node_lines.append(node_line)
                        system_b.node_lines.append(node_line)

                    if system_a.node_lines_num == len(system_a.node_lines):
                        break
                else:
                    # no system found with node slot available
                    break


TERRAIN_NAMES = [
    "Hyades",
    "Pleiades",
    "Omicron Velorum",
    "Wishing Well",
    "Ptolemy",
    "Beehive",
    "Omega",
    "Tucanae",
    "Butterfly",
    "Jewel Box",
    "Double",
    "Messier",
    "Terzan",
    "Well",
    "River",
    "Blast",
    "Cent",
    "Scutum",
    "Cygnus",
    "Norma",
    "Great Rift",
    "Great Breach",
    "Sagittarius",
    "Road",
    "Silk Path",
    "Fire",
    "Ace",
    "Glasier",
]
