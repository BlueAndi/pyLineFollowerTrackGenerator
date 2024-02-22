"""Webots VRML node Appearance
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFNode, SFString
)

class Appearance(Node): # pylint: disable=too-few-public-methods
    """Webots Appearance VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Appearance")
        self.add_fields([
            SFNode("material", None),
            SFNode("texture", None),
            SFNode("textureTransform", None),
            SFString("name", "appearance")
        ])
