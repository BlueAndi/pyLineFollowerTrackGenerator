"""Webots VRML node Lens
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec2f

class Lens(Node): # pylint: disable=too-few-public-methods
    """Webots Lens VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Lens")
        self.add_fields([
            SFVec2f("center", [ 0.5, 0.5 ]),
            SFVec2f("radialCoefficients", [ 0, 0 ]),
            SFVec2f("tangentialCoefficients", [ 0, 0 ])
        ])
