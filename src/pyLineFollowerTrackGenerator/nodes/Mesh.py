"""Webots VRML node Mesh
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFString, SFInt32, SFBool, MFString
)

class Mesh(Node): # pylint: disable=too-few-public-methods
    """Webots Mesh VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Mesh")
        self.add_fields([
            MFString("url", []),
            SFBool("ccw", True),
            SFString("name", ""),
            SFInt32("materialIndex", -1)
        ])
