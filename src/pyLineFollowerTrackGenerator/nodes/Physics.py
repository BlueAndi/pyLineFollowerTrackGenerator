"""Webots VRML node Physics
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFNode, MFVec3f, SFFloat

class Physics(Node): # pylint: disable=too-few-public-methods
    """Webots Physics VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Physics")
        self.add_fields([
            SFFloat("density", 1000),
            SFFloat("mass", -1),
            MFVec3f("centerOfMass", []),
            MFVec3f("inertiaMatrix", []),
            SFNode("damping", None)
        ])
