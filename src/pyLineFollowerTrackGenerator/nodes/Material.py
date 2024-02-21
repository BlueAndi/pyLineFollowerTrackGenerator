"""Webots VRML node Material
    This code is automatically generated. Don't modify it manually.
"""
# pylint: disable=invalid-name

from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFColor, SFFloat

class Material(Node): # pylint: disable=too-few-public-methods
    """Webots Material VRML node.
    """
    def __init__(self) -> None:
        super().__init__("Material")
        self.add_fields([
            SFFloat("ambientIntensity", 0.2),
            SFColor("diffuseColor", [ 0.8, 0.8, 0.8 ]),
            SFColor("emissiveColor", [ 0, 0, 0 ]),
            SFFloat("shininess", 0.2),
            SFColor("specularColor", [ 0, 0, 0 ]),
            SFFloat("transparency", 0)
        ])
