import random
from xml.dom import minidom
from xml.dom.minidom import Element

import xml.etree.ElementTree as ET


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
        ET.SubElement(self.root, "NumPlayers").text = str(players_num)
        ET.SubElement(self.root, "PreviewTexture")
        self.features = ET.SubElement(self.root, "Features")
        ET.SubElement(self.root, "Provinces")
        self.map_name = title if title else f"Random map {random.randint(1, 999999)}"
        map_description = description if description else "Random map"
        ET.SubElement(self.root, "Title").text = self.map_name
        ET.SubElement(self.root, "Description").text = map_description
        self.terrains = []

    def save_map(self, debug=False):
        tree = ET.ElementTree(self.root)
        file_name = self.map_name.replace(" ", "_")
        tree.write(f"{file_name}.Starmap")

        if debug:
            xmlstr = minidom.parseString(ET.tostring(self.root)).toprettyxml(indent="   ")
            with open(f"{file_name}.xml", "w") as f:
                f.write(xmlstr)
