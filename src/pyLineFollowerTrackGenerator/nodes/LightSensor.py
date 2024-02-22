"""Webots VRML node LightSensor
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    MFVec3f, SFColor, SFBool, SFFloat
)

class LightSensor(Node): # pylint: disable=too-few-public-methods
    """Webots LightSensor VRML node.
    """
    def __init__(self) -> None:
        super().__init__("LightSensor")
        self.add_fields([
            MFVec3f("lookupTable", [[0, 0, 0], [1, 1000, 0]]),
            SFColor("colorFilter", [ 1, 1, 1 ]),
            SFBool("occlusion", False),
            SFFloat("resolution", -1)
        ])
