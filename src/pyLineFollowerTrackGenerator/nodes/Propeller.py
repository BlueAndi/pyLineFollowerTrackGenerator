"""Webots VRML node Propeller
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFVec2f, SFNode, SFVec3f, SFFloat
)

class Propeller(Node): # pylint: disable=too-few-public-methods
    """Webots Propeller VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Propeller")
        self.add_fields([
            SFVec3f("shaftAxis", [ 1, 0, 0 ]),
            SFVec3f("centerOfThrust", [ 0, 0, 0 ]),
            SFVec2f("thrustConstants", [ 1, 0 ]),
            SFVec2f("torqueConstants", [ 1, 0 ]),
            SFFloat("fastHelixThreshold", 75.4),
            SFNode("device", None),
            SFNode("fastHelix", None),
            SFNode("slowHelix", None)
        ])
