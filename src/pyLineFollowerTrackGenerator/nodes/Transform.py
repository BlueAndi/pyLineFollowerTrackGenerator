"""Webots VRML node Transform
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFVec3f
)

class Transform(Node): # pylint: disable=too-few-public-methods
    """Webots Transform VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Transform")
        self.add_fields([
            SFVec3f("scale", [ 1, 1, 1 ])
        ])
