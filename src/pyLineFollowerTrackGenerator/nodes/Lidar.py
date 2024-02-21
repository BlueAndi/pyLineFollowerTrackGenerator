"""Webots VRML node Lidar
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFNode, SFString, SFInt32, SFFloat

class Lidar(Node): # pylint: disable=too-few-public-methods
    """Webots Lidar VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Lidar")
        self.add_fields([
            SFFloat("tiltAngle", 0.0),
            SFInt32("horizontalResolution", 512),
            SFFloat("fieldOfView", 1.5708),
            SFFloat("verticalFieldOfView", 0.2),
            SFInt32("numberOfLayers", 4),
            SFFloat("near", 0.01),
            SFFloat("minRange", 0.01),
            SFFloat("maxRange", 1.0),
            SFString("type", "fixed"),
            SFString("projection", "cylindrical"),
            SFFloat("noise", 0.0),
            SFFloat("resolution", -1.0),
            SFFloat("defaultFrequency", 10),
            SFFloat("minFrequency", 1),
            SFFloat("maxFrequency", 25),
            SFNode("rotatingHead", None)
        ])
