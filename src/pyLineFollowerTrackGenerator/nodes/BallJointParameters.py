"""Webots VRML node BallJointParameters
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFVec3f
)

class BallJointParameters(Node): # pylint: disable=too-few-public-methods
    """Webots BallJointParameters VRML node.
    """
    def __init__(self) -> None:
        super().__init__("BallJointParameters")
        self.add_fields([
            SFVec3f("anchor", [ 0, 0, 0 ])
        ])
