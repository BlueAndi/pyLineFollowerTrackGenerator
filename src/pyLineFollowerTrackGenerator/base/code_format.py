"""Code formatter class"""

class CodeFormat:
    """Code format parameters considers the number spaces used for indention
        and the line ending.
    """
    def __init__(self, indention = 2, line_ending = "\n") -> None:
        self._indention = indention
        self._indent_per_level = ""
        self._indent = ""
        self._line_ending = line_ending
        self._level = 0

        for _ in range(self._indention):
            self._indent_per_level += " "

    def inc_level(self) -> None:
        """Increase level of indention.
        """
        self._level += 1
        self._indent += self._indent_per_level

    def dec_level(self) -> None:
        """Decrease level of indention.
        """
        if 0 < self._level:
            self._level -= 1
            self._indent = self._indent[:-self._indention]

    def indent(self) -> str:
        """Get the number of spaces for indention by considering the current
            level.

        Returns:
            str: Number of spaces used for indention.
        """
        return self._indent

    def line_ending(self) -> str:
        """Get the line ending character(s).

        Returns:
            str: Line ending
        """
        return self._line_ending
