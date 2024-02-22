"""Webots VRML node Coordinate
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    MFVec3f
)

class Coordinate(Node): # pylint: disable=too-few-public-methods
    """Webots Coordinate VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Coordinate")
        self.add_fields([
            MFVec3f("point", [])
        ])
