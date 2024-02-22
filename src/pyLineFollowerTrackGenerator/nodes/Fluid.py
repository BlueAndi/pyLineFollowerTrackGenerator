"""Webots VRML node Fluid
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFString, SFVec3f, SFFloat, SFNode, SFBool
)

class Fluid(Node): # pylint: disable=too-few-public-methods
    """Webots Fluid VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Fluid")
        self.add_fields([
            SFString("description", ""),
            SFString("name", "fluid"),
            SFString("model", ""),
            SFString("description", ""),
            SFFloat("density", 1000),
            SFFloat("viscosity", 0.001),
            SFVec3f("streamVelocity", [ 0, 0, 0 ]),
            SFNode("boundingObject", None),
            SFBool("locked", False)
        ])
