"""Webots VRML node RotationalMotor
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFString, SFFloat
)

class RotationalMotor(Node): # pylint: disable=too-few-public-methods
    """Webots RotationalMotor VRML node.
    """
    def __init__(self) -> None:
        super().__init__("RotationalMotor")
        self.add_fields([
            SFString("name", [ "rotational, motor" ]),
            SFFloat("maxTorque", 10),
            SFString("sound", "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/default/worlds/sounds/rotational_motor.wav") # pylint: disable=line-too-long
        ])
