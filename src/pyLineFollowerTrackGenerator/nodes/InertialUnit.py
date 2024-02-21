"""Webots VRML node InertialUnit
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFBool, SFFloat

class InertialUnit(Node): # pylint: disable=too-few-public-methods
    """Webots InertialUnit VRML node.
    """
    def __init__(self) -> None:
        super().__init__("InertialUnit")
        self.add_fields([
            SFBool("xAxis", True),
            SFBool("zAxis", True),
            SFBool("yAxis", True),
            SFFloat("resolution", -1),
            SFFloat("noise", 0)
        ])
