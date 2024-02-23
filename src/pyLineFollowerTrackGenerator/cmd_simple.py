"""Command to generate a Webots world with a simple line follower track in a square arena."""

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
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splprep
from pyLineFollowerTrackGenerator.constants import Ret
from pyLineFollowerTrackGenerator.base.code_format import CodeFormat
from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec2f, SFNode
from pyLineFollowerTrackGenerator.base.world_file import WorldFile
from pyLineFollowerTrackGenerator.base.proto import Proto
from pyLineFollowerTrackGenerator.nodes.WorldInfo import WorldInfo
from pyLineFollowerTrackGenerator.nodes.Viewpoint import Viewpoint
from pyLineFollowerTrackGenerator.nodes.PBRAppearance import PBRAppearance
from pyLineFollowerTrackGenerator.nodes.ImageTexture import ImageTexture

################################################################################
# Variables
################################################################################

_CMD_NAME = "simple"

################################################################################
# Classes
################################################################################

################################################################################
# Functions
################################################################################

def _generate_points_along_rectangle(num_points, border_width, border_height): # pylint: disable=too-many-locals
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

def _generate_spline(x, y):
    num_points = len(x)

    # Generate spline representation of the line.
    # tck = A tuple (t, c, k) containing the vector of knots,
    #       the B-spline coefficients and the degree of the spline.
    tck, _ = splprep([x, y], s=0) # pylint: disable=unbalanced-tuple-unpacking

    # Generate points along the spline
    u_new = np.linspace(0, 1, num_points * 10)
    x_spline, y_spline = splev(u_new, tck, der=0)

    return x_spline, y_spline

def _generate_track_image(image_file_name, image_width, image_height, image_line_width, num_points):
    # Create figure and axis
    dpi = 100
    _, ax = plt.subplots(figsize=(image_width/dpi, image_height/dpi),dpi=dpi)

    # Set white background
    ax.set_facecolor('white')

    # Generate random line
    x, y = _generate_points_along_rectangle(num_points, image_width, image_height)
    x, y = _generate_spline(x, y)

    # Plot the line
    ax.plot(x, y, color='black', linewidth=image_line_width)

    # Set limits
    ax.set_xlim(0, image_width)
    ax.set_ylim(0, image_height)

    # Hide axes
    ax.axis('off')

    plt.savefig(image_file_name)

def _get_cmd_line_parameters() -> str:
    args = sys.argv[1:]
    cmd_line = "Parameters:"

    for arg in args:
        cmd_line += " "
        cmd_line += arg

    return cmd_line

def _exec(args): # pylint: disable=too-many-locals
    """Generate the Webots world.

    Args:
        args (obj): Program arguments

    Returns:
        Ret: If successful, it will return Ret.OK otherwise a corresponding error.
    """
    ret_status          = Ret.OK
    world_title         = args.title
    world_author        = args.author
    world_email         = args.email
    world_description   = args.desc
    world_creation_date = datetime.today().strftime('%Y-%m-%d')
    image_width         = args.imageSize # [pixel]
    image_height        = args.imageSize # [pixel]
    image_line_width    = args.imageSize * args.lineWidth / args.size # [pixel]
    arena_width         = args.size # [m]
    arena_height        = args.size # [m]
    num_points          = args.numPoints
    world_file_name     = ""
    image_file_name     = ""
    basic_time_step     = 8

    if args.worldFileName[0].endswith(".wbt") is False:
        world_file_name = args.worldFileName[0] + ".wbt"
        image_file_name = args.worldFileName[0] + ".png"
    else:
        world_file_name = args.worldFileName[0]
        image_file_name = args.worldFileName[0].replace(".wbt", ".png")

    world_info = WorldInfo()
    world_info["title"].value = world_title
    world_info["info"].values = [
        world_description,
        f"{world_author} <{world_email}>",
        world_creation_date,
        _get_cmd_line_parameters()
    ]
    world_info["basicTimeStep"].value = basic_time_step

    viewpoint = Viewpoint()
    viewpoint["orientation"].values = [0, 1, 0, np.pi / 4]
    viewpoint["position"].values = [-2 * arena_width, 0, 2 * arena_width]

    proto_textured_background = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackground.proto") # pylint: disable=line-too-long
    textured_background = Node("TexturedBackground")

    proto_textured_background_light = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackgroundLight.proto") # pylint: disable=line-too-long
    textured_background_light = Node("TexturedBackgroundLight")

    proto_rectangle_arena = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/floors/protos/RectangleArena.proto") # pylint: disable=line-too-long
    rectangle_arena = Node("RectangleArena")
    rectangle_arena.add_fields([
        SFVec2f("floorSize", [arena_width, arena_height]),
        SFVec2f("floorTileSize", [arena_width, arena_height]),
        SFNode("floorAppearance", PBRAppearance())
    ])

    rectangle_arena["floorAppearance"].value["baseColorMap"].value = ImageTexture()
    rectangle_arena["floorAppearance"].value["baseColorMap"].value["url"].values = [image_file_name]
    rectangle_arena["floorAppearance"].value["metalness"].value = 0

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

    _generate_track_image(image_file_name, image_width, image_height, image_line_width, num_points)

    code_format = CodeFormat()
    world_file.save(world_file_name, code_format)

    return ret_status

def cmd_simple_register(arg_sub_parsers):
    """Register the command specific CLI argument parser and get command
        specific paramters.

    Args:
        arg_sub_parsers (obj): Register the parser here

    Returns:
        obj: Command parameters
    """
    cmd_par_dict = {}
    cmd_par_dict["name"] = _CMD_NAME
    cmd_par_dict["execFunc"] = _exec

    parser = arg_sub_parsers.add_parser(
        "simple",
        help="Generate a Webots world with a simple line follower track in a square arena."
    )

    parser.add_argument(
        "worldFileName",
        metavar="WORLD_FILE_NAME",
        type=str,
        nargs=1,
        help="Webots world file name (.wbt)."
    )
    parser.add_argument(
        "-a",
        "--author",
        metavar="AUTHOR",
        required=False,
        default="anonymous",
        help="The authors name. (default: %(default)s)"
    )
    parser.add_argument(
        "-d",
        "--desc",
        metavar="DESC",
        required=False,
        default="Line follower track generated by pyLineFollowerTrackGenerator.",
        help="The Webots world description."
    )
    parser.add_argument(
        "-e",
        "--email",
        metavar="EMAIL",
        required=False,
        default="",
        help="The authors email address. (default: %(default)s)"
    )
    parser.add_argument(
        "-is",
        "--imageSize",
        metavar="IMAGE_SIZE",
        required=False,
        type=int,
        default=1024,
        help="The image width/length in pixel. Must be a power of 2! (default: %(default)d)"
    )
    parser.add_argument(
        "-lw",
        "--lineWidth",
        metavar="LINE_WIDTH",
        required=False,
        type=int,
        default=0.015,
        help="The arena line width in [m]. (default: %(default)d)"
    )
    parser.add_argument(
        "-np",
        "--numPoints",
        metavar="NUM_POINTS",
        required=False,
        type=int,
        default=20,
        help="The total number of points used to generate the arena. (default: %(default)d)"
    )
    parser.add_argument(
        "-s",
        "--size",
        metavar="SIZE",
        required=False,
        type=int,
        default=1,
        help="The arena width/length in [m]. (default: %(default)d)"
    )
    parser.add_argument(
        "-t",
        "--title",
        metavar="TITLE",
        required=False,
        default="my world",
        help="The world title. (default: %(default)s)"
    )

    return cmd_par_dict

################################################################################
# Main
################################################################################
