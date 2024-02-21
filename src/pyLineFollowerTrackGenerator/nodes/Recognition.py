"""Webots VRML node Recognition
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFBool, SFColor, SFInt32, SFFloat

class Recognition(Node): # pylint: disable=too-few-public-methods
    """Webots Recognition VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Recognition")
        self.add_fields([
            SFFloat("maxRange", 100),
            SFInt32("maxObjects", -1),
            SFInt32("occlusion", 1),
            SFColor("frameColor", [ 1, 0, 0 ]),
            SFInt32("frameThickness", 1),
            SFBool("segmentation", False)
        ])
