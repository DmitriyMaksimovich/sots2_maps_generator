from xml.dom.minidom import Element
import xml.etree.ElementTree as ET


class NodeLine(Element):
    def __init__(self, terrain_node_lines: ET.Element, system_a_guid: int, system_b_guid: int):
        self.terrain_node_lines = terrain_node_lines
        self.node_line = ET.SubElement(self.terrain_node_lines, "NodeLine")
        ET.SubElement(self.node_line, "SystemA").text = str(system_a_guid)
        ET.SubElement(self.node_line, "SystemB").text = str(system_b_guid)
        ET.SubElement(self.node_line, "isPermanent").text = "True"
