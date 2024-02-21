"""Webots VRML node ContactProperties
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFFloat, SFString, SFVec2f, SFInt32, MFFloat, SFVec3f

class ContactProperties(Node): # pylint: disable=too-few-public-methods
    """Webots ContactProperties VRML node.
    """
    def __init__(self) -> None:
        super().__init__("ContactProperties")
        self.add_fields([
            SFString("material1", "default"),
            SFString("material2", "default"),
            MFFloat("coulombFriction", 1),
            SFVec2f("frictionRotation", [ 0, 0 ]),
            SFVec3f("rollingFriction", [ 0, 0, 0 ]),
            SFFloat("bounce", 0.5),
            SFFloat("bounceVelocity", 0.01),
            MFFloat("forceDependentSlip", 0),
            SFFloat("softERP", 0.2),
            SFFloat("softCFM", 0.001),
            SFString("bumpSound", "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/default/worlds/sounds/bump.wav"),
            SFString("rollSound", "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/default/worlds/sounds/roll.wav"),
            SFString("slideSound", "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/default/worlds/sounds/slide.wav"),
            SFInt32("maxContactJoints", 10)
        ])
