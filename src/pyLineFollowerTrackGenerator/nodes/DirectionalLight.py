"""Webots VRML node DirectionalLight
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFVec3f
)

class DirectionalLight(Node): # pylint: disable=too-few-public-methods
    """Webots DirectionalLight VRML node.
    """
    def __init__(self) -> None:
        super().__init__("DirectionalLight")
        self.add_fields([
            SFVec3f("direction", [ 0, 0, -1 ])
        ])
