"""Webots VRML node Radar
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFBool, SFFloat
)

class Radar(Node): # pylint: disable=too-few-public-methods
    """Webots Radar VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Radar")
        self.add_fields([
            SFFloat("minRange", 1),
            SFFloat("maxRange", 50.0),
            SFFloat("horizontalFieldOfView", 0.78),
            SFFloat("verticalFieldOfView", 0.1),
            SFFloat("minAbsoluteRadialSpeed", 0.0),
            SFFloat("minRadialSpeed", 1),
            SFFloat("maxRadialSpeed", -1),
            SFFloat("cellDistance", 0.0),
            SFFloat("cellSpeed", 0.0),
            SFFloat("rangeNoise", 0.0),
            SFFloat("speedNoise", 0.0),
            SFFloat("angularNoise", 0.0),
            SFFloat("antennaGain", 20.0),
            SFFloat("frequency", 24.0),
            SFFloat("transmittedPower", 1.0),
            SFFloat("minDetectableSignal", -100),
            SFBool("occlusion", False)
        ])
