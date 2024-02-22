"""Webots VRML node Slot
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFNode, SFString
)

class Slot(Node): # pylint: disable=too-few-public-methods
    """Webots Slot VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Slot")
        self.add_fields([
            SFString("type", ""),
            SFNode("endPoint", None)
        ])
