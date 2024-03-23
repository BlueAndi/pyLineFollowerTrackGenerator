"""Command to generate a Webots world with a line follower track like a E in a square arena."""

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
import numpy as np
import matplotlib.pyplot as plt
from pyLineFollowerTrackGenerator.constants import Ret
from pyLineFollowerTrackGenerator.base.code_format import CodeFormat
from pyLineFollowerTrackGenerator.base.fields import SFString
from pyLineFollowerTrackGenerator.base.world_file import WorldFile
from pyLineFollowerTrackGenerator.base.proto import Proto
from pyLineFollowerTrackGenerator.util import (
    get_world_and_image_file_name, create_world_info,
    create_viewpoint, create_rectangle_arena,
    create_textured_background, create_textured_background_light,
    add_friction_to_world, generate_track_image
)

################################################################################
# Variables
################################################################################
_CMD_NAME = "etrack"
_NUM_OF_POINTS_MIN = 14
_BASIC_TIME_STEP = 8 # [ms]

################################################################################
# Classes
################################################################################

################################################################################
# Functions
################################################################################

# pylint: disable=too-many-locals, line-too-long
def _generate_points_along_e(num_points, rect_width, rect_height) -> list[list[int, int]]:
    """Generate a number of points along a virtual E inside a rectangle with the given
        width/height.

    Args:
        num_points (int): Number of points to generate.
        rect_width (int): Virtual rectangle width in pixels.
        rect_height (int): Virtual rectangle height in pixels.

    Returns:
        list[list[int, int]]: Point coordinates (x, y)
    """

    #        4
    #   *---------*
    #   |    2    |
    #   |  *------*
    #   |  | 2
    #   |  *------*
    # 4 |    2    |
    #   |  *------*
    #   |  | 2
    #   |  *------*
    #   |    4    |
    #   *---------*
    #
    # -----------------------> x
    #
    num_points_on_short_side = num_points // 7
    num_points_on_long_side = 2 * num_points_on_short_side
    tolerance = 10 # [%]
    width = rect_width * (100 - 2 * tolerance) // 100
    height = rect_height * (100 - 2 * tolerance) // 100
    x_tolerance = width * tolerance // 100
    y_tolerance = height * tolerance // 100
    long_ratio = 1
    short_ratio = 2/3
    distance_long_x = int(long_ratio * width / num_points_on_long_side)
    distance_long_y = int(long_ratio * height / num_points_on_long_side)
    distance_short_x = int(short_ratio * width / num_points_on_short_side)
    distance_finger = height // 5
    points = []

    # Walk along x-axis in positive direction
    y_base = 0
    for idx in range(num_points_on_long_side):
        x = idx * distance_long_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        points.append([x, y])

    # Walk along x-axis in negative direction
    x_base = width - 1
    y_base = (1 * distance_finger) - 1
    for idx in range(num_points_on_short_side):
        x = x_base - idx * distance_short_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        points.append([x, y])

    # Walk along x-axis in positive direction
    x_base = (1 - short_ratio) * width - 1
    y_base = (2 * distance_finger) - 1
    for idx in range(num_points_on_short_side):
        x = x_base + idx * distance_short_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        points.append([x, y])

    # Walk along x-axis in negative direction
    x_base = width - 1
    y_base = (3 * distance_finger) - 1
    for idx in range(num_points_on_short_side):
        x = x_base - idx * distance_short_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        points.append([x, y])

    # Walk along x-axis in positive direction
    x_base = (1 - short_ratio) * width - 1
    y_base = (4 * distance_finger) - 1
    for idx in range(num_points_on_short_side):
        x = x_base + idx * distance_short_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        points.append([x, y])

    # Walk along x-axis in negative direction
    x_base = width - 1
    y_base = (5 * distance_finger) - 1
    for idx in range(num_points_on_long_side):
        x = x_base - idx * distance_long_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        points.append([x, y])

    # Walk along y-axis in negative direction
    x_base = 0
    for idx in range(num_points_on_long_side):
        x = np.random.uniform(x_base - x_tolerance / 2, x_base + x_tolerance)
        y = y_base - idx * distance_long_y

        x += x_tolerance
        y += y_tolerance

        points.append([x, y])

    return points

# pylint: disable=too-many-locals
def _exec(args):
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
    image_width         = args.imageSize # [pixel]
    image_height        = args.imageSize # [pixel]
    image_line_width    = args.imageSize * args.lineWidth // args.size # [pixel]
    arena_width         = args.size # [m]
    arena_height        = args.size # [m]
    num_points          = args.numPoints
    pixel_per_m         = args.imageSize / args.size
    is_debug_mode       = args.debug
    material_ground     = args.materialGround
    material_robot      = args.materialRobot
    material_property   = args.materialProperty

    world_file_name, image_file_name = get_world_and_image_file_name(args.worldFileName[0])

    # Limit lower number of points to enforce that the splines can be drawn
    # within the image along the virtual rectangle.
    if num_points < _NUM_OF_POINTS_MIN:
        num_points = _NUM_OF_POINTS_MIN

        if is_debug_mode is True:
            print(f"Number of points limited to {num_points}.\n")

    world_info = create_world_info(world_title, world_description, world_author, world_email, _BASIC_TIME_STEP)
    viewpoint = create_viewpoint(arena_width, arena_height)

    proto_textured_background = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackground.proto") # pylint: disable=line-too-long
    textured_background = create_textured_background()

    proto_textured_background_light = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackgroundLight.proto") # pylint: disable=line-too-long
    textured_background_light = create_textured_background_light()

    proto_rectangle_arena = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/floors/protos/RectangleArena.proto") # pylint: disable=line-too-long
    rectangle_arena = create_rectangle_arena(arena_width, arena_height, image_file_name)

    if add_friction_to_world(world_info, material_ground, material_robot, material_property) is True:
        rectangle_arena.add_fields(
            SFString("contactMaterial", material_ground)
        )

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

    points = _generate_points_along_e(num_points, image_width, image_height)

    fig = generate_track_image( points,
                                image_width,
                                image_height,
                                image_line_width,
                                pixel_per_m,
                                is_debug_mode)

    if is_debug_mode is True:
        plt.show()

    # Save image in filesystem.
    fig.savefig(image_file_name, dpi="figure")

    code_format = CodeFormat()
    world_file.save(world_file_name, code_format)

    return ret_status

def cmd_register(arg_sub_parsers):
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
        _CMD_NAME,
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
        "-dbg",
        "--debug",
        required=False,
        default=False,
        action="store_true",
        help="Shows debug information on console and in the track."
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
        help="The arena line width in [m]. (default: %(default)f)"
    )
    parser.add_argument(
        "-mg",
        "--materialGround",
        metavar="MATERIAL_GROUND",
        required=False,
        type=str,
        default="default",
        help="The ground material used for friction. (default: %(default)s)"
    )
    parser.add_argument(
        "-mr",
        "--materialRobot",
        metavar="MATERIAL_ROBOT",
        required=False,
        type=str,
        default="default",
        help="The robot contact material (tires/track/etc.) used for friction. (default: %(default)s)"
    )
    parser.add_argument(
        "-mp",
        "--materialProperty",
        metavar="MATERIAL_PROPERTY",
        required=False,
        type=str,
        default="dry",
        help="The contact material property e.g. dry, wet, etc. used for friction. (default: %(default)s)"
    )
    parser.add_argument(
        "-np",
        "--numPoints",
        metavar="NUM_POINTS",
        required=False,
        type=int,
        default=2 * _NUM_OF_POINTS_MIN,
        help="The total number of points used to generate the arena. (default: %(default)d)"
    )
    parser.add_argument(
        "-s",
        "--size",
        metavar="SIZE",
        required=False,
        type=int,
        default=2,
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
