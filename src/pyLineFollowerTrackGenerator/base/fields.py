"""Webots VRML types"""

from typing import Union
from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.field import Field
from pyLineFollowerTrackGenerator.base.code_format import CodeFormat

class SFString(Field):
    """Single string in UTF-8 format.
    """
    def __init__(self, name: str, value: str) -> None:
        super().__init__(name)
        self.value = value

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        return f"{self.name} \"{self.value}\""

class MFString(Field):
    """Zero or more strings in UTF-8 format.
    """
    def __init__(self, name: str, values: list[str]) -> None:
        super().__init__(name)
        self.values = values

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value_list_as_str = ", ".join([f"\"{value}\"" for value in self.values])
        return f"{self.name} [ {value_list_as_str} ]"

class SFBool(Field):
    """Single boolean value.
    """
    def __init__(self, name: str, value: bool) -> None:
        super().__init__(name)
        self.value = value

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        result = "FALSE"
        if self.value is True:
            result = "TRUE"

        return f"{self.name} {result}"

class SFColor(Field):
    """Single color.
    """
    def __init__(self, name: str, values: list[float]) -> None:
        super().__init__(name)
        self.values = values

        self._sanity_check()

    def _sanity_check(self):
        if (len(self.values) % 3) != 0:
            raise ValueError("A color contains always 3 values for RGB.")

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        red = self.values[0]
        green = self.values[1]
        blue = self.values[2]

        return f"{self.name} {red} {green} {blue}"

class MFColor(Field):
    """Zero or more colors.
    """
    def __init__(self, name: str, values: Union[list[list[float]], list[float]]) -> None:
        super().__init__(name)
        self.values = values

        self._sanity_check()

    def _sanity_check(self):
        if len(self.values) > 0:
            if isinstance(self.values[0], list):
                for value in self.values:
                    if (len(value) % 3) != 0:
                        raise ValueError("A color contains always 3 values for RGB.")
            else:
                if (len(value) % 3) != 0:
                    raise ValueError("A color contains always 3 values for RGB.")

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value_list_as_str = ""

        if len(self.values) > 0:
            if isinstance(self.values[0], list):
                for index, value_list in enumerate(self.values):
                    red = value_list[0]
                    green = value_list[1]
                    blue = value_list[2]

                    if index > 0:
                        value_list_as_str += ", "

                    value_list_as_str += f"[ {red} {green} {blue} ]"
            else:
                red = self.values[0]
                green = self.values[1]
                blue = self.values[2]

                value_list_as_str += f"{red} {green} {blue}"

        return f"{self.name} [ {value_list_as_str} ]"

class SFFloat(Field):
    """One single-precision floating point number.
    """
    def __init__(self, name: str, value: float) -> None:
        super().__init__(name)
        self.value = value

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        return f"{self.name} {self.value}"

class MFFloat(Field):
    """Zero or more single-precision floating point numbers.
    """
    def __init__(self, name: str, values: list[float]) -> None:
        super().__init__(name)
        self.values = values

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value_list_as_str = ", ".join([str(value) for value in self.values])
        return f"{self.name} [ {value_list_as_str} ]"

class SFDouble(Field):
    """One double-precision floating point number.
    """
    def __init__(self, name: str, value: float) -> None:
        super().__init__(name)
        self.value = value

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        return f"{self.name} {self.value}"

class MFDouble(Field):
    """Zero or more double-precision floating point numbers.
    """
    def __init__(self, name: str, values: list[float]) -> None:
        super().__init__(name)
        self.values = values

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value_list_as_str = ", ".join([str(value) for value in self.values])
        return f"{self.name} [ {value_list_as_str} ]"

class SFInt32(Field):
    """One 32-bit integer number.
    """
    def __init__(self, name: str, value: int) -> None:
        super().__init__(name)
        self.value = value

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        return f"{self.name} {self.value}"

class MFInt32(Field):
    """Zero or more 32-bit integer numbers.
    """
    def __init__(self, name: str, values: list[int]) -> None:
        super().__init__(name)
        self.values = values

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value_list_as_str = ", ".join([str(value) for value in self.values])
        return f"{self.name} [ {value_list_as_str} ]"

class SFNode(Field):
    """One node.
    """
    def __init__(self, name: str, value: Node) -> None:
        super().__init__(name)
        self.value = value

    def export(self, code_format: CodeFormat) -> str:
        """Export to string.

        Args:
            code_format (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value = "NULL"
        if self.value is not None:
            value = self.value.export(code_format)

        return f"{self.name} {value}"

class MFNode(Field):
    """Zero or more nodes.
    """
    def __init__(self, name: str, values: list[Node]) -> None:
        super().__init__(name)
        self.values = values

    def __str__(self) -> str:
        value_list_as_str = ", ".join([str(value) for value in self.values])
        return f"{self.name} [ {value_list_as_str} ]"

    def export(self, code_format: CodeFormat) -> str:
        """Export to string.

        Args:
            code_format (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value_list_as_str = ", ".join([value.export(code_format) for value in self.values])
        return f"{self.name} [ {value_list_as_str} ]"

class SFRotation(Field):
    """One arbitrary rotation.
    """
    def __init__(self, name: str, values: list[float]) -> None:
        super().__init__(name)
        self.values = values

        self._sanity_check()

    def _sanity_check(self):
        if (len(self.values) % 4) != 0:
            raise ValueError("A rotation contains always 4 values for x, y, z and a.")

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        x = self.values[0]
        y = self.values[1]
        z = self.values[2]
        a = self.values[3]

        return f"{self.name} {x} {y} {z} {a}"

class MFRotation(Field):
    """Zero or more arbitrary rotations.
    """
    def __init__(self, name: str, values: Union[list[list[float]], list[float]]) -> None:
        super().__init__(name)
        self.values = values

        self._sanity_check()

    def _sanity_check(self):
        if len(self.values) > 0:
            if isinstance(self.values[0], list):
                for value in self.values:
                    if (len(value) % 4) != 0:
                        raise ValueError("A rotation contains always 4 values for x, y, z and a.")
            else:
                if (len(value) % 4) != 0:
                    raise ValueError("A color contains always 4 values for x, y, z and a.")

    def __str__(self) -> str:
        value_list_as_str = ""

        if len(self.values) > 0:
            if isinstance(self.values[0], list):
                for index, value_list in enumerate(self.values):
                    x = value_list[0]
                    y = value_list[1]
                    z = value_list[2]
                    a = value_list[3]

                    if index > 0:
                        value_list_as_str += ", "

                    value_list_as_str += f"[ {x} {y} {z} {a} ]"
            else:
                x = self.values[0]
                y = self.values[1]
                z = self.values[2]
                a = self.values[3]

                value_list_as_str += f"{x} {y} {z} {a}"

        return f"{self.name} [ {value_list_as_str} ]"

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value_list_as_str = ""

        if len(self.values) > 0:
            if isinstance(self.values[0], list):
                for index, value_list in enumerate(self.values):
                    x = value_list[0]
                    y = value_list[1]
                    z = value_list[2]
                    a = value_list[3]

                    if index > 0:
                        value_list_as_str += ", "

                    value_list_as_str += f"[ {x} {y} {z} {a} ]"
            else:
                x = self.values[0]
                y = self.values[1]
                z = self.values[2]
                a = self.values[3]

                value_list_as_str += f"{x} {y} {z} {a}"

        return f"{self.name} [ {value_list_as_str} ]"

class SFVec2f(Field):
    """One two-dimensional (2D) vector.
    """
    def __init__(self, name: str, values: list[float]) -> None:
        super().__init__(name)
        self.values = values

        self._sanity_check()

    def _sanity_check(self):
        if (len(self.values) % 2) != 0:
            raise ValueError("A 2D vector contains always 2 values for x and y.")

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        x = self.values[0]
        y = self.values[1]

        return f"{self.name} {x} {y}"

class MFVec2f(Field):
    """Zero or more two-dimensional (2D) vectors.
    """
    def __init__(self, name: str, values: Union[list[list[float]], list[float]]) -> None:
        super().__init__(name)
        self.values = values

        self._sanity_check()

    def _sanity_check(self):
        if len(self.values) > 0:
            if isinstance(self.values[0], list):
                for value in self.values:
                    if (len(value) % 2) != 0:
                        raise ValueError("A 2D vector contains always 2 values for x and y.")
            else:
                if (len(value) % 2) != 0:
                    raise ValueError("A 2D vector contains always 2 values for x and y.")

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value_list_as_str = ""

        if len(self.values) > 0:
            if isinstance(self.values[0], list):
                for index, value_list in enumerate(self.values):
                    x = value_list[0]
                    y = value_list[1]

                    if index > 0:
                        value_list_as_str += ", "

                    value_list_as_str += f"{x} {y}"
            else:
                x = self.values[0]
                y = self.values[1]

                value_list_as_str += f"{x} {y}"

        return f"{self.name} [ {value_list_as_str} ]"

class SFVec3f(Field):
    """One three-dimensional (3D) vector.
    """
    def __init__(self, name: str, values: list[float]) -> None:
        super().__init__(name)
        self.values = values

        self._sanity_check()

    def _sanity_check(self):
        if (len(self.values) % 3) != 0:
            raise ValueError("A 3D vector contains always 3 values for x, y and z.")

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        x = self.values[0]
        y = self.values[1]
        z = self.values[2]

        return f"{self.name} {x} {y} {z}"

class MFVec3f(Field):
    """Zero or more three-dimensional (3D) vectors.
    """
    def __init__(self, name: str, values:  Union[list[list[float]], list[float]]) -> None:
        super().__init__(name)
        self.values = values

        self._sanity_check()

    def _sanity_check(self):
        if len(self.values) > 0:
            if isinstance(self.values[0], list):
                for value in self.values:
                    if (len(value) % 3) != 0:
                        raise ValueError("A 3D vector contains always 3 values for x, y and z.")
            else:
                if (len(value) % 3) != 0:
                    raise ValueError("A 3D vector contains always 3 values for x, y and z.")

    def export(self, _: CodeFormat) -> str:
        """Export to string.

        Args:
            _ (CodeFormat): Code format used for export.

        Returns:
            str: VRML string
        """
        value_list_as_str = ""

        if len(self.values) > 0:
            if isinstance(self.values[0], list):
                for index, value_list in enumerate(self.values):
                    x = value_list[0]
                    y = value_list[1]
                    z = value_list[2]

                    if index > 0:
                        value_list_as_str += ", "

                    value_list_as_str += f"{x} {y} {z}"
            else:
                x = self.values[0]
                y = self.values[1]
                z = self.values[2]

                value_list_as_str += f"{x} {y} {z}"

        return f"{self.name} [ {value_list_as_str} ]"
