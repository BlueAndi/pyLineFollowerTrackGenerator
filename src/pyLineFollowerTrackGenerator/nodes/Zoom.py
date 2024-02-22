"""Webots VRML node Zoom
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFFloat
)

class Zoom(Node): # pylint: disable=too-few-public-methods
    """Webots Zoom VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Zoom")
        self.add_fields([
            SFFloat("maxFieldOfView", 1.5),
            SFFloat("minFieldOfView", 0.5)
        ])
