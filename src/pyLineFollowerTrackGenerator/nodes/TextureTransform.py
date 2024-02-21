"""Webots VRML node TextureTransform
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec2f, SFFloat

class TextureTransform(Node): # pylint: disable=too-few-public-methods
    """Webots TextureTransform VRML node.
    """
    def __init__(self) -> None:
        super().__init__("TextureTransform")
        self.add_fields([
            SFVec2f("center", [ 0, 0 ]),
            SFFloat("rotation", 0),
            SFVec2f("scale", [ 1, 1 ]),
            SFVec2f("translation", [ 0, 0 ])
        ])
