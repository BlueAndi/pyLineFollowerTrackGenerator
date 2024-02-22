"""Webots VRML node RangeFinder
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFInt32, SFNode, SFString, SFFloat
)

class RangeFinder(Node): # pylint: disable=too-few-public-methods
    """Webots RangeFinder VRML node.
    """
    def __init__(self) -> None:
        super().__init__("RangeFinder")
        self.add_fields([
            SFFloat("fieldOfView", 0.7854),
            SFInt32("width", 64),
            SFInt32("height", 64),
            SFString("projection", "planar"),
            SFFloat("near", 0.01),
            SFFloat("minRange", 0.01),
            SFFloat("maxRange", 1.0),
            SFFloat("motionBlur", 0.0),
            SFFloat("noise", 0.0),
            SFFloat("resolution", -1.0),
            SFNode("lens", None)
        ])
