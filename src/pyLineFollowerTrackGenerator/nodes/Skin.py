"""Webots VRML node Skin
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import MFNode, SFFloat, SFRotation, SFString, SFVec3f, SFBool

class Skin(Node): # pylint: disable=too-few-public-methods
    """Webots Skin VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Skin")
        self.add_fields([
            SFVec3f("translation", [ 0, 0, 0 ]),
            SFRotation("rotation", [ 0, 0, 1, 0 ]),
            SFVec3f("scale", [ 1, 1, 1 ]),
            SFString("name", "skin"),
            SFString("modelUrl", ""),
            MFNode("appearance", []),
            MFNode("bones", []),
            SFBool("castShadows", True),
            SFFloat("translationStep", 0.01),
            SFFloat("rotationStep", 0.261799387)
        ])
