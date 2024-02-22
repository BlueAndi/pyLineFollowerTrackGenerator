"""Webots VRML node PositionSensor
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFFloat
)

class PositionSensor(Node): # pylint: disable=too-few-public-methods
    """Webots PositionSensor VRML node.
    """
    def __init__(self) -> None:
        super().__init__("PositionSensor")
        self.add_fields([
            SFFloat("noise", 0),
            SFFloat("resolution", -1)
        ])
