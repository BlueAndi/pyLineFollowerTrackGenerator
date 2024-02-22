"""Webots VRML node SolidReference
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFString
)

class SolidReference(Node): # pylint: disable=too-few-public-methods
    """Webots SolidReference VRML node.
    """
    def __init__(self) -> None:
        super().__init__("SolidReference")
        self.add_fields([
            SFString("solidName", "")
        ])
