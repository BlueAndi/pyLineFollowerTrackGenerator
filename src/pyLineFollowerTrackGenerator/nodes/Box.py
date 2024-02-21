"""Webots VRML node Box
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec3f

class Box(Node): # pylint: disable=too-few-public-methods
    """Webots Box VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Box")
        self.add_fields([
            SFVec3f("size", [ 2, 2, 2 ])
        ])
