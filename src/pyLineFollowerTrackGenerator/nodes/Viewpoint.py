"""Webots VRML node Viewpoint
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFRotation, SFVec3f, SFFloat, SFNode, SFString
)

class Viewpoint(Node): # pylint: disable=too-few-public-methods
    """Webots Viewpoint VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Viewpoint")
        self.add_fields([
            SFFloat("fieldOfView", 0.785398),
            SFRotation("orientation", [ 0, 0, 1, 0 ]),
            SFVec3f("position", [ -10, 0, 0 ]),
            SFString("description", ""),
            SFFloat("near", 0.05),
            SFFloat("far", 0.0),
            SFFloat("exposure", 1.0),
            SFString("follow", ""),
            SFString("followType", "Tracking Shot"),
            SFFloat("followSmoothness", 0.5),
            SFNode("lensFlare", None),
            SFFloat("ambientOcclusionRadius", 2),
            SFFloat("bloomThreshold", 21)
        ])
