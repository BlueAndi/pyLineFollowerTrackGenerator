"""Webots VRML node Capsule
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFBool, SFInt32, SFFloat

class Capsule(Node): # pylint: disable=too-few-public-methods
    """Webots Capsule VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Capsule")
        self.add_fields([
            SFBool("bottom", True),
            SFFloat("height", 2),
            SFFloat("radius", 1),
            SFBool("side", True),
            SFBool("top", True),
            SFInt32("subdivision", 12)
        ])
