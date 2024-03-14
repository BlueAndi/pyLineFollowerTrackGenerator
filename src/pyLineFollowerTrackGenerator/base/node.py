"""Webots VRML base node"""

from typing import Union
from pyLineFollowerTrackGenerator.base.code_format import CodeFormat
from pyLineFollowerTrackGenerator.base.field import Field

class Node:
    """Webots VRML base node class.
    """
    def __init__(self, type_name: str) -> None:
        self.name = ""
        self._type_name = type_name
        self._field_dict = {}

    def __getitem__(self, index):
        field = None

        if isinstance(index, int):
            field = self._field_dict.items()[index]

        elif isinstance(index, str):
            field = self._field_dict[index]

        return field

    def add_fields(self, fields: Union[Field, list[Field]]) -> None:
        """Add field(s) to the node.

        Args:
            fields (union[Field, list[Field]]): One ore more fields
        """
        if isinstance(fields, list):
            for field in fields:
                self._field_dict[field.name] = field
        else:
            self._field_dict[fields.name] = fields

    def export(self, code_format: CodeFormat) -> str:
        """Export to string.

        Args:
            code_format (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        indent = code_format.indent()
        line_ending = code_format.line_ending()

        # Begin of node
        node_name = ""
        if len(self.name) > 0:
            node_name = f"DEF {self.name} "

        result = f"{node_name}{self._type_name} {{{line_ending}"

        # Add every node field
        code_format.inc_level()
        indent = code_format.indent()

        for _, field in self._field_dict.items():
            result += f"{indent}{field.export(code_format)}{line_ending}"

        code_format.dec_level()
        indent = code_format.indent()

        # End of node
        result += f"{indent}}}{line_ending}"

        return result
