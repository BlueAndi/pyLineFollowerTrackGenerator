"""Webots VRML node HingeJointParameters
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFVec3f, SFFloat
)

class HingeJointParameters(Node): # pylint: disable=too-few-public-methods
    """Webots HingeJointParameters VRML node.
    """
    def __init__(self) -> None:
        super().__init__("HingeJointParameters")
        self.add_fields([
            SFVec3f("anchor", [ 0, 0, 0 ]),
            SFVec3f("axis", [ 1, 0, 0 ]),
            SFFloat("suspensionSpringConstant", 0),
            SFFloat("suspensionDampingConstant", 0),
            SFVec3f("suspensionAxis", [ 1, 0, 0 ]),
            SFFloat("stopERP", -1),
            SFFloat("stopCFM", -1)
        ])
