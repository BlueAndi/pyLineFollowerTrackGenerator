"""Webots VRML node JointParameters
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec3f, SFFloat

class JointParameters(Node): # pylint: disable=too-few-public-methods
    """Webots JointParameters VRML node.
    """
    def __init__(self) -> None:
        super().__init__("JointParameters")
        self.add_fields([
            SFFloat("position", 0),
            SFVec3f("axis", [ 0, 0, 1 ]),
            SFFloat("minStop", 0),
            SFFloat("maxStop", 0),
            SFFloat("springConstant", 0),
            SFFloat("dampingConstant", 0),
            SFFloat("staticFriction", 0)
        ])
