"""Webots VRML node Hinge2Joint
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFNode, MFNode, SFFloat

class Hinge2Joint(Node): # pylint: disable=too-few-public-methods
    """Webots Hinge2Joint VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Hinge2Joint")
        self.add_fields([
            SFNode("jointParameters", None),
            SFNode("jointParameters2", None),
            MFNode("device2", []),
            SFFloat("position2", 0)
        ])
