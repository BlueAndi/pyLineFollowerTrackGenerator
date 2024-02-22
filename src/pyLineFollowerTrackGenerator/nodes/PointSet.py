"""Webots VRML node PointSet
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFNode
)

class PointSet(Node): # pylint: disable=too-few-public-methods
    """Webots PointSet VRML node.
    """
    def __init__(self) -> None:
        super().__init__("PointSet")
        self.add_fields([
            SFNode("color", None),
            SFNode("coord", None)
        ])
