"""The main module with the program entry point."""

# MIT License
#
# Copyright (c) 2024 Andreas Merkle (web@blue-andi.de)
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
import sys
from .constants import Ret
from .prg_arg_parser import PrgArgParser
from pyLineFollowerTrackGenerator.base.code_format import CodeFormat
from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec2f, SFNode
from pyLineFollowerTrackGenerator.base.world_file import WorldFile
from pyLineFollowerTrackGenerator.base.proto import Proto
from pyLineFollowerTrackGenerator.nodes.WorldInfo import WorldInfo
from pyLineFollowerTrackGenerator.nodes.Viewpoint import Viewpoint

from pyLineFollowerTrackGenerator.nodes.PBRAppearance import PBRAppearance
from pyLineFollowerTrackGenerator.nodes.ImageTexture import ImageTexture

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splprep

################################################################################
# Variables
################################################################################

################################################################################
# Classes
################################################################################

################################################################################
# Functions
################################################################################

def generate_points_along_rectangle(num_points, border_width, border_height):
    num_points_on_x_axis = num_points * border_width // (2 * (border_width + border_height))
    num_points_on_y_axis = num_points * border_height // (2 * (border_width + border_height))
    tolerance = 10 # [%]
    width = border_width * (100 - 2 * tolerance) // 100
    height = border_height * (100 - 2 * tolerance) // 100
    x_tolerance = width * tolerance // 100
    y_tolerance = height * tolerance // 100
    distance_x = width // num_points_on_x_axis
    distance_y = height // num_points_on_y_axis
    points_x = []
    points_y = []

    # Walk along x-axis in positive direction
    y_base = 0
    for idx in range(num_points_on_x_axis):
        x = idx * distance_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        points_x.append(x)
        points_y.append(y)

    # Walk along y-axis in positive direction
    x_base = width - 1
    for idx in range(num_points_on_y_axis):
        x = np.random.uniform(x_base - x_tolerance / 2, x_base + x_tolerance)
        y = idx * distance_y

        x += x_tolerance
        y += y_tolerance

        points_x.append(x)
        points_y.append(y)

    # Walk along x-axis in negative direction
    y_base = height - 1
    for idx in range(num_points_on_x_axis):
        x = x_base - idx * distance_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        points_x.append(x)
        points_y.append(y)

    # Walk along y-axis in negative direction
    x_base = 0
    for idx in range(num_points_on_y_axis):
        x = np.random.uniform(x_base - x_tolerance / 2, x_base + x_tolerance)
        y = y_base - idx * distance_y

        x += x_tolerance
        y += y_tolerance

        points_x.append(x)
        points_y.append(y)

    # Connect with the first point
    points_x.append(points_x[0])
    points_y.append(points_y[0])

    return points_x, points_y

def generate_spline(x, y):
    num_points = len(x)

    # Generate spline representation of the line
    tck, u = splprep([x, y], s=0)

    # Generate points along the spline
    u_new = np.linspace(0, 1, num_points * 10)
    x_spline, y_spline = splev(u_new, tck, der=0)

    return x_spline, y_spline

def draw_line_on_white_background(image_filename, width, height, line_width):
    # Create figure and axis
    dpi = 100
    _, ax = plt.subplots(figsize=(width/dpi, height/dpi),dpi=dpi)

    # Set white background
    ax.set_facecolor('white')

    # Generate random line
    x, y = generate_points_along_rectangle(20, width, height)
    x, y = generate_spline(x, y)

    # Plot the line
    ax.plot(x, y, color='black', linewidth=line_width)

    # Set limits
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)

    # Hide axes
    ax.axis('off')

    plt.savefig(image_filename)

    # Show plot
    plt.show()

def generate() -> None:
    """Generate the Webots world file.
    """
    description = "my new world generated for fun"
    author = "Andreas Merkle"
    author_email = "web@blue-andi.de"
    creation_date = "2024-02-16"
    title = "my new world"
    rectangle_arena_size_x = 10 # [m]
    rectangle_arena_size_y = 10 # [m]
    line_width = 0.015 # [m]
    image_width = 1024 # [pixel] - Must be a power of 2
    image_height = 1024 # [pixel] - Must be a power of 2
    image_line_width = image_width * line_width / rectangle_arena_size_x
    image_filename = "./track.png"

    world_info = WorldInfo()
    world_info["title"].value = title
    world_info["info"].values = [
        description,
        f"{author} <{author_email}>",
        creation_date
    ]

    viewpoint = Viewpoint()

    proto_textured_background = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackground.proto") # pylint: disable=line-too-long
    textured_background = Node("TexturedBackground")

    proto_textured_background_light = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackgroundLight.proto") # pylint: disable=line-too-long
    textured_background_light = Node("TexturedBackgroundLight")

    proto_rectangle_arena = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/floors/protos/RectangleArena.proto") # pylint: disable=line-too-long
    rectangle_arena = Node("RectangleArena")
    rectangle_arena.add_fields([
        SFVec2f("floorSize", [rectangle_arena_size_x, rectangle_arena_size_y]),
        SFVec2f("floorTileSize", [rectangle_arena_size_x, rectangle_arena_size_y]),
        SFNode("floorAppearance", PBRAppearance())
    ])

    rectangle_arena["floorAppearance"].value["baseColorMap"].value = ImageTexture()
    rectangle_arena["floorAppearance"].value["baseColorMap"].value["url"].values = [image_filename]
    rectangle_arena["floorAppearance"].value["metalness"].value = 0

    draw_line_on_white_background(image_filename, image_width, image_height, image_line_width)

    world_file = WorldFile([
        proto_textured_background,
        proto_textured_background_light,
        proto_rectangle_arena
    ], [
        world_info,
        viewpoint,
        textured_background,
        textured_background_light,
        rectangle_arena
    ])

    code_format = CodeFormat()
    world_file.save("my_world.wbt", code_format)

def main():
    """The program entry point function.

    Returns:
        int: System exit status
    """
    ret_status      = Ret.OK
    prg_arg_parser  = PrgArgParser()

    prg_arg_parser.get_sub_parsers().add_parser(
        "generate",
        help="..."
    )

    # Parse all program arguments now
    prg_arg_parser.parse_args()

    # In verbose mode print all program arguments
    if prg_arg_parser.get_args().verbose is True:
        print("Program arguments: ")
        for arg in vars(prg_arg_parser.get_args()):
            print(f"* {arg} = {vars(prg_arg_parser.get_args())[arg]}")
        print("\n")

    # If no program arguments are available, the help information shall be shown.
    if prg_arg_parser.get_args().cmd is None:
        prg_arg_parser.print_help()
    else:
        generate()

    return ret_status

################################################################################
# Main
################################################################################

if __name__ == "__main__":
    sys.exit(main())
