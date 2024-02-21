"""Generates python classes for Webots VRML nodes, derived from the markdown
    description on the Webots github project.
"""

import urllib.request
import re

WEBOTS_VERSION = "R2023b"
WEBOTS_DOCS_REFERENCE_URL = "https://raw.githubusercontent.com/cyberbotics/webots/master/docs/reference" # pylint: disable=line-too-long

def get_file_from_url(url: str) -> str:
    """Get file from given URL.

    Args:
        url (str): URL to file

    Returns:
        str: File content
    """
    with urllib.request.urlopen(url) as fd:
        content = fd.read().decode("utf-8")

    return content

def get_nodes_from_markdown(markdown: str) -> str:
    """Get the VRML nodes from the markdown description.

    Args:
        markdown (str): Markdown description of all nodes.

    Returns:
        tuple[str, str]: Tuple with node name and node markdown filename.
    """
    pattern = r"- \[(.*)\]\((.*)\)"
    return re.findall(pattern, markdown)

def get_code_from_markdown(markdown: str) -> str:
    """Get first code block from node markdown description.

    Args:
        markdown (str): Node markdown description.

    Returns:
        str: Code block
    """
    pattern = r"^```(?:\w+)?\s*\n(.*?)(?=^```)```"
    matches = re.search(pattern, markdown, re.MULTILINE | re.DOTALL)
    first_match = None

    if matches:
        first_match = matches.group(1)

    return first_match

def get_fields_from_code(code: str) -> tuple[str, str, str]:
    """Get the field type and the field name from the code block.

    Args:
        code (str): Code block

    Returns:
        tuple[str, str]: Tuple with field type and field name.
    """
    code = code.replace("field ", "") # Sometimes it looks like "  field MFString url  [ ]"
    code = code.replace("{{ webots.version.major }}", WEBOTS_VERSION)
    pattern = r"[ ]+([a-zA-Z0-9]*)[ ]+([a-zA-Z0-9]*)[ ]+([a-zA-Z0-9:/{},_<>\.\[\] \"\-]*)#?.*"
    fields = re.findall(pattern, code)
    updated_fields = []

    for field_type, field_name, field_value in fields:
        field_value = field_value.strip()

        # Boolean FALSE
        if field_value == "FALSE":
            field_value = False

        # Boolean TRUE
        elif field_value == "TRUE":
            field_value = True

        # NULL object
        elif field_value == "NULL":
            field_value = None

        # List of values [ a b c ... ] or [ a b c, d e f, ... ]
        elif (field_value.startswith("[") is True) and (field_value.endswith("]") is True):

            # List of lists with values [ a b c, d e f, ... ]
            if "," in field_value:
                value_lists = field_value[1:][:-1].split(",")

                field_value = "["
                for vl_index, value_list in enumerate(value_lists):
                    values = value_list.split()

                    if vl_index > 0:
                        field_value += ", "

                    field_value += "["
                    for index, value in enumerate(values):
                        if index > 0:
                            field_value += ", "
                        field_value += value
                    field_value += "]"
                field_value += "]"

            # List of values [ a b c ... ]
            else:
                values = field_value[1:][:-1].split()

                field_value = "["
                for index, value in enumerate(values):
                    if index > 0:
                        field_value += ", "
                    field_value += value
                field_value += "]"

        # Multiple single values: a b c ...
        else:
            values = field_value.split()

            if len(values) > 1:
                field_value = "[ "
                for index, value in enumerate(values):
                    if index > 0:
                        field_value += ", "
                    field_value += value
                field_value += " ]"

        updated_fields.append((field_type, field_name, field_value))

    return updated_fields

def generate_node_class_file(dst_folder: str, node_name: str, fields: list[tuple[str, str, str]]):
    """Generate a file with the corresponding Webots VRML node class inside.

    Args:
        node_name (str): Name of the Webots VRML node.
        fields (list[tuple[str, str, str]]): Node specific fields.
    """
    full_path = f"{dst_folder}/{node_name}.py"

    # Get unique list of field types
    unique_list_of_types = set([])
    for field_type, _, _ in fields:
        unique_list_of_types.add(field_type)

    result = f"\"\"\"Webots VRML node {node_name}\n"
    result += "    This code is automatically generated. Don't modify it manually.\n"
    result += "\"\"\"\n"
    result += "# pylint: disable=invalid-name\n"
    result += "\n"
    result += "from pyLineFollowerTrackGenerator.base.node import Node\n"

    if len(unique_list_of_types) > 0:
        result += "from pyLineFollowerTrackGenerator.base.fields import "
        for index, field_type in enumerate(unique_list_of_types):
            if index > 0:
                result += ", "
            result += field_type
        result += "\n"

    result += "\n"
    result += f"class {node_name}(Node): # pylint: disable=too-few-public-methods\n"
    result += f"    \"\"\"Webots {node_name} VRML node.\n"
    result +=  "    \"\"\"\n"
    result +=  "    def __init__(self) -> None:\n"
    result += f"        super().__init__(\"{node_name}\")\n"
    if len(fields) > 0:
        result +=  "        self.add_fields([\n"
        for index, (field_type, field_name, field_value) in enumerate(fields):
            if index > 0:
                result += ",\n"
            result += f"            {field_type}(\"{field_name}\", {field_value})"
        result += "\n"
        result +=  "        ])\n"

    with open(full_path, "w", encoding="utf-8") as file:
        file.write(result)

def main():
    """Main entry point.
    """
    url_nodes_and_api_functions = WEBOTS_DOCS_REFERENCE_URL + "/nodes-and-api-functions.md"
    ignore_list = ["Mouse", "Supervisor"]

    webots_node_markdown = get_file_from_url(url_nodes_and_api_functions)
    nodes = get_nodes_from_markdown(webots_node_markdown)

    for node_name, node_description_filename in nodes:
        if node_name in ignore_list:
            print(f"Skip {node_name}")
        else:
            print(f"Generate {node_name}")

            url_node_description = WEBOTS_DOCS_REFERENCE_URL + "/" + node_description_filename

            node_description_markdown = get_file_from_url(url_node_description)
            node_code = get_code_from_markdown(node_description_markdown)
            fields = get_fields_from_code(node_code)

            generate_node_class_file("../src/pyLineFollowerTrackGenerator/nodes", node_name, fields)

if __name__ == "__main__":
    main()
