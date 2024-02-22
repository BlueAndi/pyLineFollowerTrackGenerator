"""Webots VRML node Compass
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    MFVec3f, SFBool, SFFloat
)

class Compass(Node): # pylint: disable=too-few-public-methods
    """Webots Compass VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Compass")
        self.add_fields([
            MFVec3f("lookupTable", []),
            SFBool("xAxis", True),
            SFBool("yAxis", True),
            SFBool("zAxis", True),
            SFFloat("resolution", -1)
        ])
