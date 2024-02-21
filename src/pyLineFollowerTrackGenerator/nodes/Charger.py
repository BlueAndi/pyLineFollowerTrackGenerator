"""Webots VRML node Charger
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFFloat, SFBool, SFColor, MFFloat

class Charger(Node): # pylint: disable=too-few-public-methods
    """Webots Charger VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Charger")
        self.add_fields([
            MFFloat("battery", []),
            SFFloat("radius", 0.04),
            SFColor("emissiveColor", [ 0, 1, 0 ]),
            SFBool("gradual", True)
        ])
