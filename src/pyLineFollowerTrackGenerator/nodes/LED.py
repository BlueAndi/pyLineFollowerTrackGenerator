"""Webots VRML node LED
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFBool, MFColor
)

class LED(Node): # pylint: disable=too-few-public-methods
    """Webots LED VRML node.
    """
    def __init__(self) -> None:
        super().__init__("LED")
        self.add_fields([
            MFColor("color", [1, 0, 0]),
            SFBool("gradual", False)
        ])
