""" Webots world file
"""

from pyLineFollowerTrackGenerator.base.code_format import CodeFormat
from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.proto import Proto

class WorldFile:
    """The complete world file representation.
    """
    def __init__(self, protos: list[Proto], nodes: list[Node]) -> None:
        self._protos = protos
        self._nodes = nodes

    def _get_header(self, code_format: CodeFormat) -> str:
        line_ending = code_format.line_ending()

        return f"#VRML_SIM R2023b utf8{line_ending}{line_ending}"

    def export(self, code_format: CodeFormat) -> str:
        """Export to string.

        Args:
            code_format (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        line_ending = code_format.line_ending()

        result = self._get_header(code_format)
        result += "".join(elem.export(code_format) for elem in self._protos)
        result += f"{line_ending}"
        result += f"{line_ending}".join(elem.export(code_format) for elem in self._nodes)

        return result

    def save(self, file_name: str, code_format: CodeFormat) -> None:
        """Save world as a file.

        Args:
            file_name (str): Name of the file.
            code_format (CodeFormat): Code format used for export.
        """
        with open(file_name, "w", encoding="utf-8", newline=code_format.line_ending()) as file: # pylint: disable=line-too-long
            file.write(self.export(code_format))
