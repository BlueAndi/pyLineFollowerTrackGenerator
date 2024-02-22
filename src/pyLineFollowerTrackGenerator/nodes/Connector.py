"""Webots VRML node Connector
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFInt32, SFBool, SFString, SFFloat
)

class Connector(Node): # pylint: disable=too-few-public-methods
    """Webots Connector VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Connector")
        self.add_fields([
            SFString("type", "symmetric"),
            SFBool("isLocked", False),
            SFBool("autoLock", False),
            SFBool("unilateralLock", True),
            SFBool("unilateralUnlock", True),
            SFFloat("distanceTolerance", 0.01),
            SFFloat("axisTolerance", 0.2),
            SFFloat("rotationTolerance", 0.2),
            SFInt32("numberOfRotations", 4),
            SFBool("snap", True),
            SFFloat("tensileStrength", -1),
            SFFloat("shearStrength", -1)
        ])
