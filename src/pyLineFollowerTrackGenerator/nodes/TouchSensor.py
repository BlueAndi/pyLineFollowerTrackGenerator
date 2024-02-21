"""Webots VRML node TouchSensor
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import MFVec3f, SFString, SFFloat

class TouchSensor(Node): # pylint: disable=too-few-public-methods
    """Webots TouchSensor VRML node.
    """
    def __init__(self) -> None:
        super().__init__("TouchSensor")
        self.add_fields([
            SFString("type", "bumper"),
            MFVec3f("lookupTable", [[0, 0, 0], [5000, 50000, 0]]),
            SFFloat("resolution", -1)
        ])
