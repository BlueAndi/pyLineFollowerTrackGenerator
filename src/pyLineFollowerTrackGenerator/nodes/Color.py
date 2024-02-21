"""Webots VRML node Color
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import MFColor

class Color(Node): # pylint: disable=too-few-public-methods
    """Webots Color VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Color")
        self.add_fields([
            MFColor("color", [])
        ])
