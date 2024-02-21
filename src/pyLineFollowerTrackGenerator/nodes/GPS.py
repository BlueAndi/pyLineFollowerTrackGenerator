"""Webots VRML node GPS
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFString, SFFloat

class GPS(Node): # pylint: disable=too-few-public-methods
    """Webots GPS VRML node.
    """
    def __init__(self) -> None:
        super().__init__("GPS")
        self.add_fields([
            SFString("type", "satellite"),
            SFFloat("accuracy", 0),
            SFFloat("noiseCorrelation", 0),
            SFFloat("resolution", -1),
            SFFloat("speedNoise", 0),
            SFFloat("speedResolution", -1)
        ])
