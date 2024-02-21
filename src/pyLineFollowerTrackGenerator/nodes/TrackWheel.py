"""Webots VRML node TrackWheel
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFBool, SFVec2f, SFFloat

class TrackWheel(Node): # pylint: disable=too-few-public-methods
    """Webots TrackWheel VRML node.
    """
    def __init__(self) -> None:
        super().__init__("TrackWheel")
        self.add_fields([
            SFVec2f("position", [ 0, 0 ]),
            SFFloat("radius", 0.1),
            SFBool("inner", True)
        ])
