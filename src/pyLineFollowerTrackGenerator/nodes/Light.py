"""Webots VRML node Light
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFBool, SFColor, SFFloat

class Light(Node): # pylint: disable=too-few-public-methods
    """Webots Light VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Light")
        self.add_fields([
            SFFloat("ambientIntensity", 0),
            SFColor("color", [ 1, 1, 1 ]),
            SFFloat("intensity", 1),
            SFBool("on", True),
            SFBool("castShadows", False)
        ])
