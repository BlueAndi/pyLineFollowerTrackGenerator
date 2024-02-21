"""Webots VRML node LinearMotor
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFString, SFFloat

class LinearMotor(Node): # pylint: disable=too-few-public-methods
    """Webots LinearMotor VRML node.
    """
    def __init__(self) -> None:
        super().__init__("LinearMotor")
        self.add_fields([
            SFString("name", [ "linear, motor" ]),
            SFFloat("maxForce", 10),
            SFString("sound", "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/default/worlds/sounds/linear_motor.wav")
        ])
