"""Webots VRML node DistanceSensor
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFInt32, MFVec3f, SFString, SFFloat

class DistanceSensor(Node): # pylint: disable=too-few-public-methods
    """Webots DistanceSensor VRML node.
    """
    def __init__(self) -> None:
        super().__init__("DistanceSensor")
        self.add_fields([
            MFVec3f("lookupTable", [[0, 0, 0], [0.1, 1000, 0]]),
            SFString("type", "generic"),
            SFInt32("numberOfRays", 1),
            SFFloat("aperture", 1.5708),
            SFFloat("gaussianWidth", 1),
            SFFloat("resolution", -1),
            SFFloat("redColorSensitivity", 1)
        ])
