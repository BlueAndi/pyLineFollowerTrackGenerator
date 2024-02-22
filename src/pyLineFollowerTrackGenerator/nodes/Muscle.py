"""Webots VRML node Muscle
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFBool, MFColor, SFDouble, SFVec3f
)

class Muscle(Node): # pylint: disable=too-few-public-methods
    """Webots Muscle VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Muscle")
        self.add_fields([
            SFDouble("volume", 0.01),
            SFVec3f("startOffset", [ 0, 0, 0 ]),
            SFVec3f("endOffset", [ 0, 0, 0 ]),
            MFColor("color", []),
            SFBool("castShadows", True),
            SFBool("visible", True)
        ])
