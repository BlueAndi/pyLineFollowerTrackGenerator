"""Webots VRML node Pen
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFColor, SFBool, SFFloat
)

class Pen(Node): # pylint: disable=too-few-public-methods
    """Webots Pen VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Pen")
        self.add_fields([
            SFColor("inkColor", [ 0, 0, 0 ]),
            SFFloat("inkDensity", 0.5),
            SFFloat("leadSize", 0.002),
            SFFloat("maxDistance", 0.0),
            SFBool("write", True)
        ])
