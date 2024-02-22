"""Webots VRML node TextureCoordinate
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    MFVec2f
)

class TextureCoordinate(Node): # pylint: disable=too-few-public-methods
    """Webots TextureCoordinate VRML node.
    """
    def __init__(self) -> None:
        super().__init__("TextureCoordinate")
        self.add_fields([
            MFVec2f("point", [])
        ])
