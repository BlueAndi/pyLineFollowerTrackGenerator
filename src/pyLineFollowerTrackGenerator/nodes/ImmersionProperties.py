"""Webots VRML node ImmersionProperties
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec3f, SFString, SFFloat

class ImmersionProperties(Node): # pylint: disable=too-few-public-methods
    """Webots ImmersionProperties VRML node.
    """
    def __init__(self) -> None:
        super().__init__("ImmersionProperties")
        self.add_fields([
            SFString("fluidName", ""),
            SFString("referenceArea", [ "immersed, area" ]),
            SFVec3f("dragForceCoefficients", [ 0, 0, 0 ]),
            SFVec3f("dragTorqueCoefficients", [ 0, 0, 0 ]),
            SFFloat("viscousResistanceForceCoefficient", 0),
            SFFloat("viscousResistanceTorqueCoefficient", 0)
        ])
