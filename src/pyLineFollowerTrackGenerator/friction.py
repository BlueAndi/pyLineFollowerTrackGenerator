"""This module contains the program argument parser and its configuration."""

# MIT License
#
# Copyright (c) 2022 - 2024 Andreas Merkle (web@blue-andi.de)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

################################################################################
# Imports
################################################################################
import json
import random
from typing import Union

################################################################################
# Variables
################################################################################
FRICTION_FILE_NAME = "./database/friction.json"

################################################################################
# Classes
################################################################################

class Friction():
    """Provivdes the friction data of two materials.
        The friction data itself is loaded from an external database in JSON format.
    """

    def __init__(self):
        self._friction_data = {}

    def _load(self, file_name: str) -> bool:
        status = False

        try:
            with open(file_name, encoding="utf-8") as json_data:
                self._friction_data = json.load(json_data)

            status = self._check_friction_data()

            if status is False:
                self._friction_data = {}

        except FileNotFoundError:
            print(f"{file_name} not found.")

        return status

    def _check_friction_data(self) -> bool:
        status = True

        if "friction" not in self._friction_data:
            print("No friction data available.")
            status = False
        else:
            for idx, material_pair in enumerate(self._friction_data["friction"]):
                if "material1" not in material_pair:
                    print(f"[{idx}] Material 1 is missing.")
                    status = False
                elif "material2" not in material_pair:
                    print(f"[{idx}] Material 2 is missing.")
                    status = False

        return status

    def _print_friction(self, kind_of, indention) -> None:
        for key, value in kind_of.items():
            if isinstance(value, dict):
                min_value = value["min"]
                max_value = value["max"]
                print(f"{indention}{key}: {min_value} - {max_value}")
            else:
                print(f"{indention}{key}: {value}")

    def _print_material_pair(self, material_pair) -> None:
        material1 = material_pair["material1"]
        material2 = material_pair["material2"]

        print(f"\"{material1}\" - \"{material2}\"")

        print(f"{self._indention(1)}static friction:")
        if "static" in material_pair:
            self._print_friction(material_pair["static"], self._indention(2))
        else:
            print(f"{self._indention(2)}no data")

        print(f"{self._indention(1)}sliding friction:")
        if "sliding" in material_pair:
            self._print_friction(material_pair["sliding"], self._indention(2))
        else:
            print(f"{self._indention(2)}no data")

    def _indention(self, level) -> str:
        indention = ""
        for _ in range(level * 4):
            indention += " "

        return indention

    def load(self) -> bool:
        """Load friction data from JSON file.

        Returns:
            bool: If successful loaded, it will return True otherwise False.
        """
        return self._load(FRICTION_FILE_NAME)

    def print_all(self) -> None:
        """Print the whole friction data to console.
        """
        if "friction" in self._friction_data:
            for idx, material_pair in enumerate(self._friction_data["friction"]):
                if 0 < idx:
                    print("")

                self._print_material_pair(material_pair)

    def print_filtered_by_material(self, material: str) -> None:
        """Print the friction data of the material to console.
        """
        if "friction" in self._friction_data:
            count = 0

            for material_pair in self._friction_data["friction"]:
                if material in (material_pair["material1"], material_pair["material2"]):
                    if 0 < count:
                        print("")

                    self._print_material_pair(material_pair)

                    count += 1

    # pylint: disable=line-too-long
    def get_friction(self, material1: str, material2: str, material_property: str) -> tuple[Union[None,float], Union[None,float]]:
        """Get friction between the two materials and by considering whether its
            e.g. dry.

        Args:
            material1 (str): Name of material 1
            material2 (str): Name of material 2
            material_property (str): Material property like e.g. dry, wet, etc.

        Returns:
            tuple[Union[None,float], Union[None,float]]: If material pair found,
                                    it will return the friction (static, dynamic), otherwise None.
        """
        static_friction_value = None
        dynamic_friction_value = None

        if "friction" in self._friction_data:
            for material_pair in self._friction_data["friction"]:
                if material1 in (material_pair["material1"], material_pair["material2"]):
                    if material2 in (material_pair["material1"], material_pair["material2"]):

                        if "static" in material_pair:
                            if material_property in material_pair["static"]:
                                friction = material_pair["static"][material_property]
                                if isinstance(friction, dict):
                                    friction_min = friction["min"]
                                    friction_max = friction["max"]
                                    static_friction_value = random.uniform(friction_min, friction_max)
                                else:
                                    static_friction_value = friction

                        if "sliding" in material_pair:
                            if material_property in material_pair["sliding"]:
                                friction = material_pair["sliding"][material_property]
                                if isinstance(friction, dict):
                                    friction_min = friction["min"]
                                    friction_max = friction["max"]
                                    dynamic_friction_value = random.uniform(friction_min, friction_max)
                                else:
                                    dynamic_friction_value = friction

        return (static_friction_value, dynamic_friction_value)

################################################################################
# Functions
################################################################################

################################################################################
# Main
################################################################################
