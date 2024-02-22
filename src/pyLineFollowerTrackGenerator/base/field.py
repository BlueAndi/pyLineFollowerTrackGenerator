"""Webots VRML base field"""

class Field: # pylint: disable=too-few-public-methods
    """Base field
    """
    def __init__(self, name: str) -> None:
        self.name = name
