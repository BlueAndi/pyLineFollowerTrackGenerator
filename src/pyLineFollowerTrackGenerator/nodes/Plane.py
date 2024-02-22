"""Webots VRML node Plane
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFVec2f
)

class Plane(Node): # pylint: disable=too-few-public-methods
    """Webots Plane VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Plane")
        self.add_fields([
            SFVec2f("size", [ 1, 1 ])
        ])
