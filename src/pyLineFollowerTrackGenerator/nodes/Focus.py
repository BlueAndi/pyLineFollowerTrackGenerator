"""Webots VRML node Focus
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFFloat

class Focus(Node): # pylint: disable=too-few-public-methods
    """Webots Focus VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Focus")
        self.add_fields([
            SFFloat("focalDistance", 0),
            SFFloat("focalLength", 0),
            SFFloat("maxFocalDistance", 0),
            SFFloat("minFocalDistance", 0)
        ])
