"""Command to generate a Webots world with a line follower track in a square arena,
    defined by the user in a grid with a fixed point to point length.
"""

# MIT License
#
# Copyright (c) 2024 - 2025 Andreas Merkle (web@blue-andi.de)
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
from typing import Any
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep
from pyLineFollowerTrackGenerator.constants import Ret
from pyLineFollowerTrackGenerator.base.code_format import CodeFormat
from pyLineFollowerTrackGenerator.base.fields import SFString
from pyLineFollowerTrackGenerator.base.world_file import WorldFile
from pyLineFollowerTrackGenerator.base.proto import Proto
from pyLineFollowerTrackGenerator.util import (
    get_world_and_image_file_name, create_world_info,
    create_viewpoint, create_rectangle_arena,
    create_textured_background, create_textured_background_light,
    add_friction_to_world, generate_start_stop_line, get_start_stop_line_width,
    get_start_stop_line_distance_to_middle
)

# pylint: disable=R0801

################################################################################
# Variables
################################################################################
_CMD_NAME = "grid"
_NUM_OF_POINTS_MIN = 2
_BASIC_TIME_STEP = 8 # [ms]

_QUADRANT = [
    # dx, dy, quadrant
    ( 1,  1, 1),
    (-1,  1, 2),
    (-1, -1, 3),
    ( 1, -1, 4)
]

_ANGLES = [
    # direction vector (x, y)   quadrant    angle start, end    new direction

    ( 0,  1,    1,      1/2 * np.pi,    1   * np.pi,     1,  0),    # north / curve to right / west
    (-1,  0,    1,      0   * np.pi,    0   * np.pi,     0,  0),    # west / n.a. / n.a.
    ( 0, -1,    1,      0   * np.pi,    0   * np.pi,     0,  0),    # south / n.a. / n. a.
    ( 1,  0,    1,      3/2 * np.pi,    2   * np.pi,     0,  1),    # east / curve to left / north

    ( 0,  1,    2,      0   * np.pi,    1/2 * np.pi,    -1,  0),    # north / curve to left / west
    (-1,  0,    2,      1   * np.pi,    3/2 * np.pi,     0,  1),    # west / curve to right / north
    ( 0, -1,    2,      0   * np.pi,    0   * np.pi,     0,  0),    # south / n.a. / n.a.
    ( 1,  0,    2,      0   * np.pi,    0   * np.pi,     0,  0),    # east / n.a. / n.a.

    ( 0,  1,    3,      0   * np.pi,    0   * np.pi,     0,  0),    # north / n.a. / n.a.
    (-1,  0,    3,      1/2 * np.pi,    1   * np.pi,     0, -1),    # west / curve to left / south
    ( 0, -1,    3,      1/2 * np.pi,    1   * np.pi,    -1,  0),    # south / curve to right / west
    ( 1,  0,    3,      0   * np.pi,    0   * np.pi,     0,  0),    # east / n.a. / n.a.

    ( 0,  1,    4,      0   * np.pi,    0   * np.pi,     0,  0),    # north / n.a. / n.a.
    (-1,  0,    4,      0   * np.pi,    0   * np.pi,     0,  0),    # west / n.a. / n.a.
    ( 0, -1,    4,      1   * np.pi,    3/2 * np.pi,     1,  0),    # south / curve to left / east
    ( 1,  0,    4,      0   * np.pi,    1/2 * np.pi,     0, -1),    # east / curve to right / south
]

_CENTER = [
    # direction vector (x, y)   quadrant    point x, point y

    ( 0,  1,    1,      "e", "s"),  # north / curve to right / x from end point / y from start point
    (-1,  0,    1,      "", ""),    # west / n.a. / n.a. / n.a.
    ( 0, -1,    1,      "", ""),    # south / n.a. / n.a. / n.a.
    ( 1,  0,    1,      "s", "e"),  # east / curve to left / x from start point / y from end point

    ( 0,  1,    2,      "e", "s"),  # north / curve to left / x from end point / y from start point
    (-1,  0,    2,      "s", "e"),  # west / curve to right / x from start point / y from end point
    ( 0, -1,    2,      "", ""),    # south / n.a. / n.a. / n.a.
    ( 1,  0,    2,      "", ""),    # east / n.a. / n.a. / n.a.

    ( 0,  1,    3,      "", ""),    # north / n.a. / n.a. / n.a.
    (-1,  0,    3,      "s", "e"),  # west / curve to left / x from start point / y from end point
    ( 0, -1,    3,      "e", "s"),  # south / curve to right / x from end point / y from start point
    ( 1,  0,    3,      "", ""),    # east / n.a. / n.a. / n.a.

    ( 0,  1,    4,      "", ""),    # north / n.a. / n.a. / n.a.
    (-1,  0,    4,      "", ""),    # west / n.a. / n.a. / n.a.
    ( 0, -1,    4,      "e", "s"),  # south / curve to left / x from end point / y from start point
    ( 1,  0,    4,      "s", "e"),  # east / curve to right / x from start point / y from end point
]

################################################################################
# Classes
################################################################################

################################################################################
# Functions
################################################################################

def _determine_quadrant(dx: int, dy: int):
    for (delta_x, delta_y, quadrant) in _QUADRANT:
        if (delta_x == dx) and (delta_y == dy):
            return quadrant

    return 0

# pylint: disable=line-too-long
def _determine_angles(dir_vec_x: int, dir_vec_y: int, quadrant: int) -> tuple[float, float, int, int]:
    for (d_vec_x, d_vec_y, q, angle_start, angle_end, dir_vec_x_new, dir_vec_y_new) in _ANGLES:
        if (d_vec_x == dir_vec_x) and (d_vec_y == dir_vec_y):
            if q == quadrant:
                return angle_start, angle_end, dir_vec_x_new, dir_vec_y_new

    return 0, 0, 0, 0

def _normalize(value):
    if 0 < value:
        normalized_value = 1
    elif 0 > value:
        normalized_value = -1
    else:
        normalized_value = 0

    return normalized_value

def _determine_center(dir_vec_x: int, dir_vec_y: int, quadrant: int, point_start: list[int], point_end: list[int]) -> list[int]:
    center_point = [0, 0]

    for (d_vec_x, d_vec_y, q, x_source, y_source) in _CENTER:
        if (d_vec_x == dir_vec_x) and (d_vec_y == dir_vec_y):
            if q == quadrant:
                if "s" == x_source:
                    center_point[0] = point_start[0]
                else:
                    center_point[0] = point_end[0]

                if "s" == y_source:
                    center_point[1] = point_start[1]
                else:
                    center_point[1] = point_end[1]

    return center_point

# pylint: disable=too-many-arguments, line-too-long
def _plot_circle(ax: Any, center: list[int], radius: int, start_angle: float, end_angle: float, line_width: int, color: str) -> Any:
    angles = np.linspace(start_angle, end_angle, 100)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return ax.plot(x, y, color=color, linewidth=line_width)

def _determine_direction(dx: int, dy: int) -> tuple[int, int]:
    if 0 < dx:
        dir_vec_x = 1
    elif 0 > dx:
        dir_vec_x = -1
    else:
        dir_vec_x = 0

    if 0 < dy:
        dir_vec_y = 1
    elif 0 > dy:
        dir_vec_y = -1
    else:
        dir_vec_y = 0

    return dir_vec_x, dir_vec_y

# pylint: disable=too-many-arguments, line-too-long, too-many-locals, too-many-branches, too-many-statements
def generate_track_image(points: list[list[int]], image_width: int, image_height: int, image_line_width: int, grid_point_distance: float, pixel_per_m: float, start_stop_line_locations: list[bool], is_debug_mode: bool) -> plt.Figure:
    """Generate the image with the line follower track.

    Args:
        points (list[list[int]]): List of points in the grid.
        image_width (int): Image width in pixels.
        image_height (int): Image height in pixels.
        image_line_width (int): The line follower line width in pixels.
        grid_point_distance (int): The distance between two points in the grid in pixel.
        pixel_per_m (float): Conversion factor pixel per m.
        start_stop_line_locations (list[bool]): Locations of start-/stop-line.
        is_debug_mode (bool): In debug mode the image will get additional information.

    Returns:
        plt.Figure: Figure
    """
    line_color = "black"
    line_points_color = "red"
    start_stop_line_color = line_color
    background_color = "white"

    # In debug mode show the start-/stop-line in different color.
    if is_debug_mode is True:
        start_stop_line_color = "orange"

    # Create figure and axis.
    dpi = 72 # Use a dpi of 72 to plot with exact pixel sizes.
    fig, ax = plt.subplots(figsize=(image_width/dpi, image_height/dpi), dpi=dpi)

    # Set background color.
    ax.set_facecolor(background_color)

    # Plot the line.
    border_size = 10 # [%]
    border_x = image_width * (2 * border_size) // 100
    border_y = image_height * (2 * border_size) // 100
    point_start = None
    point_end = None
    dir_vec_x = 1
    dir_vec_y = 0

    for point, start_stop_line_location in zip(points, start_stop_line_locations):
        # Consider grid point distance
        point[0] *= grid_point_distance
        point[1] *= grid_point_distance
        # Consider border
        point[0] += border_x
        point[1] += border_y

        if point_start is None:
            point_start = point
        else:
            point_end = point

        if (point_start is not None) and (point_end is not None):
            dx = point_end[0] - point_start[0]
            dy = point_end[1] - point_start[1]

            # Draw a line?
            if (0 == dx) or (0 == dy):
                line, = ax.plot([point_start[0], point_end[0]], [point_start[1], point_end[1]], color=line_color, linewidth=image_line_width, zorder=1)
                dir_vec_x, dir_vec_y = _determine_direction(dx, dy)

            else:
                normalized_dx = _normalize(dx)
                normalized_dy = _normalize(dy)
                quadrant = _determine_quadrant(normalized_dx, normalized_dy)
                angle_start, angle_end, dir_vec_x_new, dir_vec_y_new = _determine_angles(dir_vec_x, dir_vec_y, quadrant)
                center_point = _determine_center(dir_vec_x, dir_vec_y, quadrant, point_start, point_end)
                radius = abs(dx)

                line, = _plot_circle(ax, center_point, radius, angle_start, angle_end, image_line_width, line_color)

                dir_vec_x = dir_vec_x_new
                dir_vec_y = dir_vec_y_new

            # Plot start- and stop-line
            if start_stop_line_location is True:
                x_data = line.get_xdata()
                y_data = line.get_ydata()

                # Fit a spline to the line data.
                tck, _ = splprep([x_data, y_data], k=min(3, len(x_data) - 1), s=0) # pylint: disable=unbalanced-tuple-unpacking

                # Plot start- and stop-line
                x_perpendicular_low, y_perpendicular_low, \
                x_perpendicular_high, y_perpendicular_high = \
                    generate_start_stop_line(   tck,
                                                0,
                                                int(get_start_stop_line_distance_to_middle() * pixel_per_m),
                                                int(get_start_stop_line_width() * pixel_per_m))

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

            point_start = point_end
            point_end = None

    # Show the points used for generation in debug mode.
    if is_debug_mode is True:

        # Convert the points to separate x- and y-coordinates.
        x_points = [point[0] for point in points]
        y_points = [point[1] for point in points]

        ax.scatter(x_points, y_points, color=line_points_color, linewidth=image_line_width, zorder=2)

    # Set limits
    ax.set_xlim(0, image_width)
    ax.set_ylim(0, image_height)

    # Set aspect ratio to ensure that a unit on x-axis is equal to a unit on y-axis.
    ax.set_aspect("equal", adjustable="box")

    # Hide axes
    ax.axis('off')

    return fig

def _load_grid(file_name: str) -> tuple[list[list[int]], list[bool]]:
    grid_points = []
    start_stop_line_points = []

    try:
        with open(file_name, encoding="utf-8") as fd:
            data = json.load(fd)

        for point in data["track"]:
            start_stop_line = False

            if "startStopLine" in point:
                start_stop_line = True

            grid_points.append([point["x"], point["y"]])
            start_stop_line_points.append(start_stop_line)

    except FileNotFoundError:
        pass

    return grid_points, start_stop_line_points

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
    pixel_per_m         = args.imageSize / args.size # [pixel/m]
    grid_point_distance = args.pointDistance * pixel_per_m # [pixel]
    is_debug_mode       = args.debug
    material_ground     = args.materialGround
    material_robot      = args.materialRobot
    material_property   = args.materialProperty

    world_file_name, image_file_name = get_world_and_image_file_name(args.worldFileName[0])

    world_info = create_world_info(world_title, world_description, world_author, world_email, _BASIC_TIME_STEP)
    viewpoint = create_viewpoint(arena_width, arena_height)

    proto_textured_background = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2025a/projects/objects/backgrounds/protos/TexturedBackground.proto") # pylint: disable=line-too-long
    textured_background = create_textured_background()

    proto_textured_background_light = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2025a/projects/objects/backgrounds/protos/TexturedBackgroundLight.proto") # pylint: disable=line-too-long
    textured_background_light = create_textured_background_light()

    proto_rectangle_arena = Proto("https://raw.githubusercontent.com/cyberbotics/webots/R2025a/projects/objects/floors/protos/RectangleArena.proto") # pylint: disable=line-too-long
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

    points, start_stop_line_locations = _load_grid(args.gridFileName[0])

    if len(points) < _NUM_OF_POINTS_MIN:
        print(f"Min. number of points are {_NUM_OF_POINTS_MIN}.\n")
        ret_status = Ret.ERROR
    else:
        fig = generate_track_image( points,
                                    image_width,
                                    image_height,
                                    image_line_width,
                                    grid_point_distance,
                                    pixel_per_m,
                                    start_stop_line_locations,
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
        help="Generate a Webots world with a line follower track in a square arena." \
            "The track is defined by a JSON file and uses a grid with fixed distance."
    )

    parser.add_argument(
        "worldFileName",
        metavar="WORLD_FILE_NAME",
        type=str,
        nargs=1,
        help="Webots world file name (.wbt)."
    )
    parser.add_argument(
        "gridFileName",
        metavar="GRID_FILE_NAME",
        type=str,
        nargs=1,
        help="Grid file name (.json)."
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
        "-pd",
        "--pointDistance",
        metavar="POINT_DISTANCE",
        required=False,
        type=float,
        default=0.1,
        help="The point distance in the grid in [m]. (default: %(default)f)"
    )
    parser.add_argument(
        "-is",
        "--imageSize",
        metavar="IMAGE_SIZE",
        required=False,
        type=int,
        default=2048,
        help="The image width/length in pixel. Must be a power of 2! (default: %(default)d)"
    )
    parser.add_argument(
        "-lw",
        "--lineWidth",
        metavar="LINE_WIDTH",
        required=False,
        type=float,
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
