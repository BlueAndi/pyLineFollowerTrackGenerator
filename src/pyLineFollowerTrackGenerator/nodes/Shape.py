"""Webots VRML node Shape
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFNode, SFBool
)

class Shape(Node): # pylint: disable=too-few-public-methods
    """Webots Shape VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Shape")
        self.add_fields([
            SFNode("appearance", None),
            SFNode("geometry", None),
            SFBool("castShadows", True),
            SFBool("isPickable", True)
        ])
