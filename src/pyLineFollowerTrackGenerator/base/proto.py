"""Webots VRML prototype"""

from pyLineFollowerTrackGenerator.base.code_format import CodeFormat

class Proto: # pylint: disable=too-few-public-methods
    """Webots VRML prototype
    """
    def __init__(self, url: str) -> None:
        self._url = url

    def export(self, code_format: CodeFormat) -> str:
        """Export to string.

        Args:
            code_format (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        return f"EXTERNPROTO \"{self._url}\"{code_format.line_ending()}"
