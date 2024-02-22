"""Webots VRML node Sphere
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFInt32, SFBool, SFFloat
)

class Sphere(Node): # pylint: disable=too-few-public-methods
    """Webots Sphere VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Sphere")
        self.add_fields([
            SFFloat("radius", 1),
            SFInt32("subdivision", 1),
            SFBool("ico", True)
        ])
