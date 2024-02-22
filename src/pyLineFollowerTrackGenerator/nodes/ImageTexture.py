"""Webots VRML node ImageTexture
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFInt32, SFBool, MFString
)

class ImageTexture(Node): # pylint: disable=too-few-public-methods
    """Webots ImageTexture VRML node.
    """
    def __init__(self) -> None:
        super().__init__("ImageTexture")
        self.add_fields([
            MFString("url", []),
            SFBool("repeatS", True),
            SFBool("repeatT", True),
            SFInt32("filtering", 4)
        ])
