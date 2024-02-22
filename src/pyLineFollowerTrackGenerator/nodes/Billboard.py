"""Webots VRML node Billboard
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    MFNode
)

class Billboard(Node): # pylint: disable=too-few-public-methods
    """Webots Billboard VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Billboard")
        self.add_fields([
            MFNode("children", [])
        ])
