"""Webots VRML node HingeJoint
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import MFNode, SFFloat

class HingeJoint(Node): # pylint: disable=too-few-public-methods
    """Webots HingeJoint VRML node.
    """
    def __init__(self) -> None:
        super().__init__("HingeJoint")
        self.add_fields([
            MFNode("device", []),
            SFFloat("position", 0)
        ])
