"""Webots VRML node VacuumGripper
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFBool, SFInt32, SFFloat

class VacuumGripper(Node): # pylint: disable=too-few-public-methods
    """Webots VacuumGripper VRML node.
    """
    def __init__(self) -> None:
        super().__init__("VacuumGripper")
        self.add_fields([
            SFBool("isOn", False),
            SFFloat("tensileStrength", -1),
            SFFloat("shearStrength", -1),
            SFInt32("contactPoints", 3)
        ])
