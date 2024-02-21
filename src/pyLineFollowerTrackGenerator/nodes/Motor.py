"""Webots VRML node Motor
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import MFNode, SFVec3f, SFString, SFFloat

class Motor(Node): # pylint: disable=too-few-public-methods
    """Webots Motor VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Motor")
        self.add_fields([
            SFFloat("acceleration", -1),
            SFFloat("consumptionFactor", 10),
            SFVec3f("controlPID", [ 10, 0, 0 ]),
            SFFloat("minPosition", 0),
            SFFloat("maxPosition", 0),
            SFFloat("maxVelocity", 10),
            SFFloat("multiplier", 1),
            SFString("sound", ""),
            MFNode("muscles", [])
        ])
