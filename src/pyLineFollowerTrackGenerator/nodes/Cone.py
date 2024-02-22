"""Webots VRML node Cone
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFInt32, SFBool, SFFloat
)

class Cone(Node): # pylint: disable=too-few-public-methods
    """Webots Cone VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Cone")
        self.add_fields([
            SFFloat("bottomRadius", 1),
            SFFloat("height", 2),
            SFBool("side", True),
            SFBool("bottom", True),
            SFInt32("subdivision", 12)
        ])
