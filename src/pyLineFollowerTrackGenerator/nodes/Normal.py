"""Webots VRML node Normal
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    MFVec3f
)

class Normal(Node): # pylint: disable=too-few-public-methods
    """Webots Normal VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Normal")
        self.add_fields([
            MFVec3f("vector", [])
        ])
