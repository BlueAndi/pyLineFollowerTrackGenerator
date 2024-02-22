"""Webots VRML node Altimeter
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFString, SFFloat
)

class Altimeter(Node): # pylint: disable=too-few-public-methods
    """Webots Altimeter VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Altimeter")
        self.add_fields([
            SFString("name", "altimeter"),
            SFFloat("accuracy", 0),
            SFFloat("resolution", -1)
        ])
