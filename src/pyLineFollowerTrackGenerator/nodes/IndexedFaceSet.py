"""Webots VRML node IndexedFaceSet
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFNode, SFBool, MFInt32, SFFloat

class IndexedFaceSet(Node): # pylint: disable=too-few-public-methods
    """Webots IndexedFaceSet VRML node.
    """
    def __init__(self) -> None:
        super().__init__("IndexedFaceSet")
        self.add_fields([
            SFNode("coord", None),
            SFNode("normal", None),
            SFNode("texCoord", None),
            SFBool("solid", True),
            SFBool("ccw", True),
            SFBool("convex", True),
            SFBool("normalPerVertex", True),
            MFInt32("coordIndex", []),
            MFInt32("normalIndex", []),
            MFInt32("texCoordIndex", []),
            SFFloat("creaseAngle", 0)
        ])
