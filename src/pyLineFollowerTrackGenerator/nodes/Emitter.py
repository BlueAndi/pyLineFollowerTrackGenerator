"""Webots VRML node Emitter
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    MFInt32, SFInt32, SFString, SFFloat
)

class Emitter(Node): # pylint: disable=too-few-public-methods
    """Webots Emitter VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Emitter")
        self.add_fields([
            SFString("type", "radio"),
            SFFloat("range", -1),
            SFFloat("maxRange", -1),
            SFFloat("aperture", -1),
            SFInt32("channel", 0),
            SFInt32("baudRate", -1),
            SFInt32("byteSize", 8),
            SFInt32("bufferSize", -1),
            MFInt32("allowedChannels", [])
        ])
