"""Webots VRML node Damping
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFFloat
)

class Damping(Node): # pylint: disable=too-few-public-methods
    """Webots Damping VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Damping")
        self.add_fields([
            SFFloat("linear", 0.2),
            SFFloat("angular", 0.2)
        ])
