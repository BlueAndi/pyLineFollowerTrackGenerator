"""Webots VRML node ElevationGrid
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import (
    SFInt32, MFFloat, SFFloat
)

class ElevationGrid(Node): # pylint: disable=too-few-public-methods
    """Webots ElevationGrid VRML node.
    """
    def __init__(self) -> None:
        super().__init__("ElevationGrid")
        self.add_fields([
            MFFloat("height", []),
            SFInt32("xDimension", 0),
            SFFloat("xSpacing", 1),
            SFInt32("yDimension", 0),
            SFFloat("ySpacing", 1),
            SFFloat("thickness", 1)
        ])
