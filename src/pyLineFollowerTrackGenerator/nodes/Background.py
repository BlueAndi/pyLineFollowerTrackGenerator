"""Webots VRML node Background
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFFloat, MFColor, MFString

class Background(Node): # pylint: disable=too-few-public-methods
    """Webots Background VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Background")
        self.add_fields([
            MFColor("skyColor", [0, 0, 0]),
            MFString("backUrl", []),
            MFString("bottomUrl", []),
            MFString("frontUrl", []),
            MFString("leftUrl", []),
            MFString("rightUrl", []),
            MFString("topUrl", []),
            MFString("backIrradianceUrl", []),
            MFString("bottomIrradianceUrl", []),
            MFString("frontIrradianceUrl", []),
            MFString("leftIrradianceUrl", []),
            MFString("rightIrradianceUrl", []),
            MFString("topIrradianceUrl", []),
            SFFloat("luminosity", 1)
        ])
