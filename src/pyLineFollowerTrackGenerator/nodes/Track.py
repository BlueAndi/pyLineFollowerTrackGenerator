"""Webots VRML node Track
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFNode, MFNode, SFInt32, SFVec2f

class Track(Node): # pylint: disable=too-few-public-methods
    """Webots Track VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Track")
        self.add_fields([
            MFNode("device", []),
            SFVec2f("textureAnimation", [ 0, 0 ]),
            SFNode("animatedGeometry", None),
            SFInt32("geometriesCount", 10)
        ])
