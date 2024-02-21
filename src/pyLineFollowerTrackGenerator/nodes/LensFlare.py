"""Webots VRML node LensFlare
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFInt32, SFFloat

class LensFlare(Node): # pylint: disable=too-few-public-methods
    """Webots LensFlare VRML node.
    """
    def __init__(self) -> None:
        super().__init__("LensFlare")
        self.add_fields([
            SFFloat("transparency", 0.4),
            SFFloat("scale", 1.5),
            SFFloat("bias", -0.9),
            SFFloat("dispersal", 0.6),
            SFInt32("samples", 4),
            SFFloat("haloWidth", 0.4),
            SFFloat("chromaDistortion", 2.0),
            SFInt32("blurIterations", 2)
        ])
