"""Webots VRML node PointLight
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec3f, SFFloat

class PointLight(Node): # pylint: disable=too-few-public-methods
    """Webots PointLight VRML node.
    """
    def __init__(self) -> None:
        super().__init__("PointLight")
        self.add_fields([
            SFVec3f("attenuation", [ 1, 0, 0 ]),
            SFVec3f("location", [ 0, 0, 0 ]),
            SFFloat("radius", 100)
        ])
