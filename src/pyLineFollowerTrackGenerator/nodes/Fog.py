"""Webots VRML node Fog
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFColor, SFString, SFFloat
)

class Fog(Node): # pylint: disable=too-few-public-methods
    """Webots Fog VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Fog")
        self.add_fields([
            SFColor("color", [ 1, 1, 1 ]),
            SFString("fogType", "LINEAR"),
            SFFloat("visibilityRange", 0)
        ])
