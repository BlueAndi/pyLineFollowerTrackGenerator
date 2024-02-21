"""Webots VRML node WorldInfo
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFNode, MFNode, SFFloat, SFString, MFString, SFInt32, SFVec3f

class WorldInfo(Node): # pylint: disable=too-few-public-methods
    """Webots WorldInfo VRML node.
    """
    def __init__(self) -> None:
        super().__init__("WorldInfo")
        self.add_fields([
            SFString("title", ""),
            MFString("info", []),
            SFString("window", "<none>"),
            SFFloat("gravity", 9.81),
            SFFloat("CFM", 0.00001),
            SFFloat("ERP", 0.2),
            SFString("physics", "<none>"),
            SFFloat("basicTimeStep", 32),
            SFFloat("FPS", 60),
            SFInt32("optimalThreadCount", 1),
            SFFloat("physicsDisableTime", 1),
            SFFloat("physicsDisableLinearThreshold", 0.01),
            SFFloat("physicsDisableAngularThreshold", 0.01),
            SFNode("defaultDamping", None),
            SFFloat("inkEvaporation", 0),
            SFString("coordinateSystem", "ENU"),
            SFString("gpsCoordinateSystem", "local"),
            SFVec3f("gpsReference", [ 0, 0, 0 ]),
            SFFloat("lineScale", 0.1),
            SFFloat("dragForceScale", 30.0),
            SFFloat("dragTorqueScale", 5.0),
            SFInt32("randomSeed", 0),
            MFNode("contactProperties", [])
        ])
