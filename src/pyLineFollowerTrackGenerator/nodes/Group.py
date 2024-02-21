"""Webots VRML node Group
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import MFNode

class Group(Node): # pylint: disable=too-few-public-methods
    """Webots Group VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Group")
        self.add_fields([
            MFNode("children", [])
        ])
