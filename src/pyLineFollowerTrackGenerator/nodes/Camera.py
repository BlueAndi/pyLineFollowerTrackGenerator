"""Webots VRML node Camera
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFInt32, SFString, SFFloat, SFNode, SFBool
)

class Camera(Node): # pylint: disable=too-few-public-methods
    """Webots Camera VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Camera")
        self.add_fields([
            SFFloat("fieldOfView", 0.7854),
            SFInt32("width", 64),
            SFInt32("height", 64),
            SFString("projection", "planar"),
            SFFloat("near", 0.01),
            SFFloat("far", 0.0),
            SFFloat("exposure", 1.0),
            SFBool("antiAliasing", False),
            SFFloat("ambientOcclusionRadius", 0),
            SFFloat("bloomThreshold", -1.0),
            SFFloat("motionBlur", 0.0),
            SFFloat("noise", 0.0),
            SFString("noiseMaskUrl", ""),
            SFNode("lens", None),
            SFNode("focus", None),
            SFNode("zoom", None),
            SFNode("recognition", None),
            SFNode("lensFlare", None)
        ])
