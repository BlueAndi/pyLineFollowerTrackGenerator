"""Webots VRML node Display
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFInt32
)

class Display(Node): # pylint: disable=too-few-public-methods
    """Webots Display VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Display")
        self.add_fields([
            SFInt32("width", 64),
            SFInt32("height", 64)
        ])
