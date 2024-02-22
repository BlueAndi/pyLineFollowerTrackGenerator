"""Webots VRML node BallJoint
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFNode, MFNode, SFFloat
)

class BallJoint(Node): # pylint: disable=too-few-public-methods
    """Webots BallJoint VRML node.
    """
    def __init__(self) -> None:
        super().__init__("BallJoint")
        self.add_fields([
            SFNode("jointParameters", None),
            SFNode("jointParameters2", None),
            SFNode("jointParameters3", None),
            MFNode("device3", []),
            SFFloat("position3", 0)
        ])
