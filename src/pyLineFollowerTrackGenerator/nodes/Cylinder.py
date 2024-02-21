"""Webots VRML node Cylinder
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFBool, SFInt32, SFFloat

class Cylinder(Node): # pylint: disable=too-few-public-methods
    """Webots Cylinder VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Cylinder")
        self.add_fields([
            SFBool("bottom", True),
            SFFloat("height", 2),
            SFFloat("radius", 1),
            SFBool("side", True),
            SFBool("top", True),
            SFInt32("subdivision", 12)
        ])
