"""Webots VRML node Solid
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFNode, MFNode, SFFloat, SFString, MFColor, SFVec3f, SFBool

class Solid(Node): # pylint: disable=too-few-public-methods
    """Webots Solid VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Solid")
        self.add_fields([
            SFString("name", "solid"),
            SFString("model", ""),
            SFString("description", ""),
            SFString("contactMaterial", "default"),
            MFNode("immersionProperties", []),
            SFNode("boundingObject", None),
            SFNode("physics", None),
            SFBool("locked", False),
            SFFloat("radarCrossSection", 0.0),
            MFColor("recognitionColors", []),
            SFVec3f("linearVelocity", [ 0, 0, 0 ]),
            SFVec3f("angularVelocity", [ 0, 0, 0 ])
        ])
