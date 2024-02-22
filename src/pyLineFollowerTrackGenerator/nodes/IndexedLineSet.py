"""Webots VRML node IndexedLineSet
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    MFInt32, SFNode
)

class IndexedLineSet(Node): # pylint: disable=too-few-public-methods
    """Webots IndexedLineSet VRML node.
    """
    def __init__(self) -> None:
        super().__init__("IndexedLineSet")
        self.add_fields([
            SFNode("coord", None),
            MFInt32("coordIndex", [])
        ])
