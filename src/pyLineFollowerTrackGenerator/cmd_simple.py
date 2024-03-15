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
from typing import Union
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splprep
from pyLineFollowerTrackGenerator.constants import Ret
from pyLineFollowerTrackGenerator.base.code_format import CodeFormat
from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec2f, SFNode, SFString
from pyLineFollowerTrackGenerator.base.world_file import WorldFile
from pyLineFollowerTrackGenerator.base.proto import Proto
from pyLineFollowerTrackGenerator.nodes.WorldInfo import WorldInfo
from pyLineFollowerTrackGenerator.nodes.Viewpoint import Viewpoint
from pyLineFollowerTrackGenerator.nodes.PBRAppearance import PBRAppearance
from pyLineFollowerTrackGenerator.nodes.ImageTexture import ImageTexture
from pyLineFollowerTrackGenerator.nodes.ContactProperties import ContactProperties
from pyLineFollowerTrackGenerator.friction import Friction

################################################################################
# Variables
################################################################################
_CMD_NAME = "simple"
_START_STOP_LINE_WIDTH = 0.05 # [m]
_START_STOP_LINE_DISTANCE_TO_MIDDLE = 0.025 # [m]
_NUM_OF_POINTS_MIN = 8
_BASIC_TIME_STEP = 8 # [ms]

################################################################################
# Classes
################################################################################

################################################################################
# Functions
################################################################################

# pylint: disable=too-many-locals, line-too-long
def _generate_points_along_rectangle(num_points, rect_width, rect_height) -> tuple[list[int], list[int]]:
    """Generate a number of points along a virtual rectangle with the given
        width/height.

    Args:
        num_points (int): Number of points to generate.
        rect_width (int): Virtual rectangle width in pixels.
        rect_height (int): Virtual rectangle height in pixels.

    Returns:
        tuple[list[int], list[int]]: Point coordinates (x, y)
    """
    num_points_on_x_axis = num_points * rect_width // (2 * (rect_width + rect_height))
    num_points_on_y_axis = num_points * rect_height // (2 * (rect_width + rect_height))
    tolerance = 10 # [%]
    width = rect_width * (100 - 2 * tolerance) // 100
    height = rect_height * (100 - 2 * tolerance) // 100
    x_tolerance = width * tolerance // 100
    y_tolerance = height * tolerance // 100
    distance_x = width // num_points_on_x_axis
    distance_y = height // num_points_on_y_axis
    x_points = []
    y_points = []

    # Walk along x-axis in positive direction
    y_base = 0
    for idx in range(num_points_on_x_axis):
        x = idx * distance_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        x_points.append(x)
        y_points.append(y)

    # Walk along y-axis in positive direction
    x_base = width - 1
    for idx in range(num_points_on_y_axis):
        x = np.random.uniform(x_base - x_tolerance / 2, x_base + x_tolerance)
        y = idx * distance_y

        x += x_tolerance
        y += y_tolerance

        x_points.append(x)
        y_points.append(y)

    # Walk along x-axis in negative direction
    y_base = height - 1
    for idx in range(num_points_on_x_axis):
        x = x_base - idx * distance_x
        y = np.random.uniform(y_base - y_tolerance / 2, y_base + y_tolerance)

        x += x_tolerance
        y += y_tolerance

        x_points.append(x)
        y_points.append(y)

    # Walk along y-axis in negative direction
    x_base = 0
    for idx in range(num_points_on_y_axis):
        x = np.random.uniform(x_base - x_tolerance / 2, x_base + x_tolerance)
        y = y_base - idx * distance_y

        x += x_tolerance
        y += y_tolerance

        x_points.append(x)
        y_points.append(y)

    return x_points, y_points

def _generate_spline(x, y):
    num_points = len(x)

    # Generate spline representation of the line.
    # The line will be like a closed track.
    # tck = A tuple (t, c, k) containing the vector of knots,
    #       the B-spline coefficients and the degree of the spline.
    tck, _ = splprep([x, y], s=0, per=True) # pylint: disable=unbalanced-tuple-unpacking

    # Generate points along the spline
    u_new = np.linspace(0, 1, num_points * 10)
    x_spline, y_spline = splev(u_new, tck, der=0)

    return x_spline, y_spline, tck

def _generate_start_stop_line(tck, u, distance_from_middle, length) -> tuple[list[float], list[float], list[float], list[float]]:
    """Generate points for a start-/stop-line. The start-/stop-line
        start at the given distance from the line middle on both
        sides and has a dediacted length.

    Args:
        tck (tuple(t,c,k)): Knots vector
        u (float): Location on the virtual rectangle spline [0..1]
        distance_from_middle (int): Distance from the line middle in pixels.
        length (int): Length in pixels of one part of the start-/stop-line.

    Returns:
        tuple[list[float], list[float], list[float], list[float]]: Lower and upper points of the start-/stop-line.
    """
    # Calculate the derivative of the spline at the given parameter u.
    dx, dy = splev(u, tck, der=1)

    # Determine the point on the spline at the given parameter u.
    x_spline, y_spline = splev(u, tck)

    # Determine the unit normal vector to the tangent
    mag = np.sqrt(dx**2 + dy**2)
    nx = -dy / mag  # x-component of the unit normal vector
    ny = dx / mag   # y-component of the unit normal vector

    # Determine the points on the perpendicular lines to form
    x_perpendicular_low = [
        x_spline - distance_from_middle * nx,
        x_spline - (distance_from_middle + length) * nx
    ]
    y_perpendicular_low = [
        y_spline - distance_from_middle * ny,
        y_spline - (distance_from_middle + length) * ny
    ]

    x_perpendicular_high = [
        x_spline + distance_from_middle * nx,
        x_spline + (distance_from_middle + length) * nx
    ]
    y_perpendicular_high = [
        y_spline + distance_from_middle * ny,
        y_spline + (distance_from_middle + length) * ny
    ]

    return x_perpendicular_low, y_perpendicular_low, x_perpendicular_high, y_perpendicular_high

# pylint: disable=too-many-arguments, line-too-long
def _generate_track_image(num_points, image_width, image_height, image_line_width, pixel_per_m, is_debug_mode) -> plt.Figure:
    """Generate the image with the line follower track.

    Args:
        num_points (int): Number of points on the used virtual rectangle.
        image_width (int): Image width in pixels.
        image_height (int): Image height in pixels.
        image_line_width (int): The line follower line width in pixels.
        pixel_per_m (float): Conversion factor pixel per m.
        is_debug_mode (bool): In debug mode the image will get additional information.

    Returns:
        plt.Figure: Figure
    """
    line_color = "black"
    line_points_color = "red"
    start_stop_line_color = line_color
    background_color = "white"

    # 12.5 % after the first point, means in the middle of the lower rectangle part.
    start_stop_line_location = 0.125

    # In debug mode show the start-/stop-line in different color.
    if is_debug_mode is True:
        start_stop_line_color = "orange"

    # Create figure and axis
    dpi = 72 # Use a dpi of 72 to plot with exact pixel sizes.
    fig, ax = plt.subplots(figsize=(image_width/dpi, image_height/dpi),dpi=dpi)

    # Set background color
    ax.set_facecolor(background_color)

    # Generate random line
    x_rect, y_rect = _generate_points_along_rectangle(num_points, image_width, image_height)
    x_spline, y_spline, tck = _generate_spline(x_rect, y_rect)

    # Plot the line
    ax.plot(x_spline, y_spline, color=line_color, linewidth=image_line_width, zorder=1)

    # Show the points used for generation in debug mode.
    if is_debug_mode is True:
        ax.scatter(x_rect, y_rect, color=line_points_color, linewidth=image_line_width, zorder=2)

    # Plot start- and stop-line
    x_perpendicular_low, y_perpendicular_low, \
    x_perpendicular_high, y_perpendicular_high = \
        _generate_start_stop_line(  tck,
                                    start_stop_line_location,
                                    _START_STOP_LINE_DISTANCE_TO_MIDDLE * pixel_per_m,
                                    _START_STOP_LINE_WIDTH * pixel_per_m)

    ax.plot(x_perpendicular_low,
            y_perpendicular_low,
            color=start_stop_line_color,
            linewidth=image_line_width,
            zorder=2)
    ax.plot(x_perpendicular_high,
            y_perpendicular_high,
            color=start_stop_line_color,
            linewidth=image_line_width,
            zorder=2)

    # Set limits
    ax.set_xlim(0, image_width)
    ax.set_ylim(0, image_height)

    # Hide axes
    ax.axis('off')

    return fig

def _get_cmd_line_parameters() -> str:
    args = sys.argv[1:]
    cmd_line = "Parameters:"

    for arg in args:
        cmd_line += " "
        cmd_line += arg

    return cmd_line

def _get_world_and_image_file_name(user_world_file_name: str) -> tuple[str, str]:
    world_file_name = ""
    image_file_name = ""

    if user_world_file_name.endswith(".wbt") is False:
        world_file_name = user_world_file_name + ".wbt"
        image_file_name = user_world_file_name + ".png"
    else:
        world_file_name = user_world_file_name
        image_file_name = user_world_file_name.replace(".wbt", ".png")

    return (world_file_name, image_file_name)

def _create_world_info(title: str, description: str, author: str, author_email: str) -> WorldInfo:
    world_creation_date = datetime.today().strftime('%Y-%m-%d')

    world_info = WorldInfo()
    world_info["title"].value = title
    world_info["info"].values = [
        description,
        f"{author} <{author_email}>",
        world_creation_date,
        _get_cmd_line_parameters()
    ]
    world_info["basicTimeStep"].value = _BASIC_TIME_STEP

    return world_info

def _create_viewpoint(arena_width: float, arena_height: float) -> Viewpoint:
    viewpoint = Viewpoint()
    viewpoint["orientation"].values = [0, 1, 0, np.pi / 4]
    viewpoint["position"].values = [-2 * arena_width, 0, 2 * arena_height]

    return viewpoint

def _create_textured_background() -> Node:
    return Node("TexturedBackground")

def _create_textured_background_light() -> Node:
    return Node("TexturedBackgroundLight")

def _create_rectangle_arena(arena_width: float, arena_height: float, image_file_name) -> Node:
    rectangle_arena = Node("RectangleArena")
    rectangle_arena.add_fields([
        SFVec2f("floorSize", [arena_width, arena_height]),
        SFVec2f("floorTileSize", [arena_width, arena_height]),
        SFNode("floorAppearance", PBRAppearance())
    ])

    rectangle_arena["floorAppearance"].value["baseColorMap"].value = ImageTexture()
    rectangle_arena["floorAppearance"].value["baseColorMap"].value["url"].values = [image_file_name]
    rectangle_arena["floorAppearance"].value["metalness"].value = 0

    return rectangle_arena

def _create_contact_properties(material_ground: str, material_robot: str, static_friction: Union[None,float], dynamic_friction: Union[None,float]) -> ContactProperties:
    contact_properties = ContactProperties()
    contact_properties["material1"].value = material_ground
    contact_properties["material2"].value = material_robot

    if static_friction is not None:
        contact_properties["coulombFriction"].values = [static_friction]

    if dynamic_friction is not None:
        contact_properties["forceDependentSlip"].values = [dynamic_friction]

    return contact_properties

def _add_friction_to_world(world_info, material_ground: str, material_robot: str, material_property: str) -> bool:
    status = False

    if (material_ground != "default") or (material_robot != "default"):
        friction_db = Friction()

        if friction_db.load() is True:
            static_friction, dynamic_friction = friction_db.get_friction(material_ground, material_robot, material_property)

            if static_friction is None:
                print(f"Static friction for {material_ground} / {material_robot}: -")
            else:
                print(f"Static friction for {material_ground} / {material_robot}: {static_friction}")

            if dynamic_friction is None:
                print(f"Dynamic friction for {material_ground} / {material_robot}: -")
            else:
                print(f"Dynamic friction for {material_ground} / {material_robot}: {dynamic_friction}")

            if (static_friction is not None) or (dynamic_friction is not None):
                contact_properties = _create_contact_properties(material_ground, material_robot, static_friction, dynamic_friction)
                world_info["contactProperties"].values = [contact_properties]
                status = True

    return status

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

    world_file_name, image_file_name = _get_world_and_image_file_name(args.worldFileName[0])

    # Limit lower number of points to enforce that the splines can be drawn
    # within the image along the virtual rectangle.
    if num_points < _NUM_OF_POINTS_MIN:
        num_points = _NUM_OF_POINTS_MIN

        if is_debug_mode is True:
            print(f"Number of points limited to {num_points}.\n")

    world_info = _create_world_info(world_title, world_description, world_author, world_email)
    viewpoint = _create_viewpoint(arena_width, arena_height)

    proto_textured_background = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackground.proto") # pylint: disable=line-too-long
    textured_background = _create_textured_background()

    proto_textured_background_light = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackgroundLight.proto") # pylint: disable=line-too-long
    textured_background_light = _create_textured_background_light()

    proto_rectangle_arena = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/floors/protos/RectangleArena.proto") # pylint: disable=line-too-long
    rectangle_arena = _create_rectangle_arena(arena_width, arena_height, image_file_name)

    if _add_friction_to_world(world_info, material_ground, material_robot, material_property) is True:
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

    fig = _generate_track_image(num_points,
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
        help="The arena line width in [m]. (default: %(default)d)"
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
