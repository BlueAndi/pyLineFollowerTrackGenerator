"""Webots VRML node Receiver
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import MFInt32, SFString, SFInt32, SFFloat

class Receiver(Node): # pylint: disable=too-few-public-methods
    """Webots Receiver VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Receiver")
        self.add_fields([
            SFString("type", "radio"),
            SFFloat("aperture", -1),
            SFInt32("channel", 0),
            SFInt32("baudRate", -1),
            SFInt32("byteSize", 8),
            SFInt32("bufferSize", -1),
            SFFloat("signalStrengthNoise", 0),
            SFFloat("directionNoise", 0),
            MFInt32("allowedChannels", [])
        ])
