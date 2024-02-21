"""Webots VRML node SpotLight
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec3f, SFColor, SFBool, SFFloat

class SpotLight(Node): # pylint: disable=too-few-public-methods
    """Webots SpotLight VRML node.
    """
    def __init__(self) -> None:
        super().__init__("SpotLight")
        self.add_fields([
            SFFloat("ambientIntensity", 0),
            SFVec3f("attenuation", [ 1, 0, 0 ]),
            SFFloat("beamWidth", 1.570796),
            SFColor("color", [ 1, 1, 1 ]),
            SFFloat("cutOffAngle", 0.785398),
            SFVec3f("direction", [ 0, 0, -1 ]),
            SFFloat("intensity", 1),
            SFVec3f("location", [ 0, 0, 10 ]),
            SFBool("on", True),
            SFFloat("radius", 100),
            SFBool("castShadows", False)
        ])
