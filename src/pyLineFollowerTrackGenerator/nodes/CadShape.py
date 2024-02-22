"""Webots VRML node CadShape
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFBool, MFString
)

class CadShape(Node): # pylint: disable=too-few-public-methods
    """Webots CadShape VRML node.
    """
    def __init__(self) -> None:
        super().__init__("CadShape")
        self.add_fields([
            MFString("url", []),
            SFBool("ccw", True),
            SFBool("castShadows", True),
            SFBool("isPickable", True)
        ])
