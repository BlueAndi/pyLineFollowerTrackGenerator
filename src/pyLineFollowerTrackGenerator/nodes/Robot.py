"""Webots VRML node Robot
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFFloat, SFString, MFString, MFFloat, SFBool

class Robot(Node): # pylint: disable=too-few-public-methods
    """Webots Robot VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Robot")
        self.add_fields([
            SFString("controller", "<generic>"),
            MFString("controllerArgs", []),
            SFString("customData", ""),
            SFBool("supervisor", False),
            SFBool("synchronization", True),
            MFFloat("battery", []),
            SFFloat("cpuConsumption", 10),
            SFBool("selfCollision", False),
            SFString("window", "<generic>"),
            SFString("remoteControl", "<none>")
        ])
