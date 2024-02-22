"""Webots VRML node Gyro
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    MFVec3f, SFBool, SFFloat
)

class Gyro(Node): # pylint: disable=too-few-public-methods
    """Webots Gyro VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Gyro")
        self.add_fields([
            MFVec3f("lookupTable", []),
            SFBool("xAxis", True),
            SFBool("yAxis", True),
            SFBool("zAxis", True),
            SFFloat("resolution", -1)
        ])
