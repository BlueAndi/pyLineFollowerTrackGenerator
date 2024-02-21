"""Webots VRML node PBRAppearance
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFNode, SFFloat, SFString, SFColor

class PBRAppearance(Node): # pylint: disable=too-few-public-methods
    """Webots PBRAppearance VRML node.
    """
    def __init__(self) -> None:
        super().__init__("PBRAppearance")
        self.add_fields([
            SFColor("baseColor", [ 1, 1, 1 ]),
            SFNode("baseColorMap", None),
            SFFloat("transparency", 0),
            SFFloat("roughness", 0),
            SFNode("roughnessMap", None),
            SFFloat("metalness", 1),
            SFNode("metalnessMap", None),
            SFFloat("IBLStrength", 1),
            SFNode("normalMap", None),
            SFFloat("normalMapFactor", 1),
            SFNode("occlusionMap", None),
            SFFloat("occlusionMapStrength", 1),
            SFColor("emissiveColor", [ 0, 0, 0 ]),
            SFNode("emissiveColorMap", None),
            SFFloat("emissiveIntensity", 1),
            SFNode("textureTransform", None),
            SFString("name", "PBRAppearance")
        ])
