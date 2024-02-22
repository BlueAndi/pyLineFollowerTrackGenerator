"""Webots VRML node Joint
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFNode
)

class Joint(Node): # pylint: disable=too-few-public-methods
    """Webots Joint VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Joint")
        self.add_fields([
            SFNode("jointParameters", None),
            SFNode("endPoint", None)
        ])
