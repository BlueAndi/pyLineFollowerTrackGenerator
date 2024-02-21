"""Webots VRML node Accelerometer
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFBool, MFVec3f, SFString, SFFloat

class Accelerometer(Node): # pylint: disable=too-few-public-methods
    """Webots Accelerometer VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Accelerometer")
        self.add_fields([
            SFString("name", "accelerometer"),
            MFVec3f("lookupTable", []),
            SFBool("xAxis", True),
            SFBool("yAxis", True),
            SFBool("zAxis", True),
            SFFloat("resolution", -1)
        ])
