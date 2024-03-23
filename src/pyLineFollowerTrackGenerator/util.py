"""Utilitiy functionality."""

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
from pyLineFollowerTrackGenerator.base.node import Node
from pyLineFollowerTrackGenerator.base.fields import SFVec2f, SFNode
from pyLineFollowerTrackGenerator.nodes.WorldInfo import WorldInfo
from pyLineFollowerTrackGenerator.nodes.Viewpoint import Viewpoint
from pyLineFollowerTrackGenerator.nodes.PBRAppearance import PBRAppearance
from pyLineFollowerTrackGenerator.nodes.ImageTexture import ImageTexture
from pyLineFollowerTrackGenerator.nodes.ContactProperties import ContactProperties
from pyLineFollowerTrackGenerator.friction import Friction

################################################################################
# Variables
################################################################################
_START_STOP_LINE_WIDTH = 0.05 # [m]
_START_STOP_LINE_DISTANCE_TO_MIDDLE = 0.025 # [m]

################################################################################
# Classes
################################################################################

################################################################################
# Functions
################################################################################

def generate_spline(points: list[tuple[float, float]]):
    """Generate splines through list of points.

    Args:
        points (list[tuple[float, float]]): Points with x- and y-coordinate.

    Returns:
        tuple[list[float], list[float], tuple]:
            List of arrays representing the curve in an N-D space.
            Vector of knots, the B-spline coefficients, and the degree of the spline.
    """
    num_points = len(points)

    # Convert the points to separate x- and y-coordinates.
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    # Generate spline representation of the line.
    # The line will be like a closed track.
    # tck = A tuple (t, c, k) containing the vector of knots,
    #       the B-spline coefficients and the degree of the spline.
    tck, _ = splprep([x, y], s=0, per=True) # pylint: disable=unbalanced-tuple-unpacking

    # Generate points along the spline
    u_new = np.linspace(0, 1, num_points * 10)
    x_spline, y_spline = splev(u_new, tck, der=0)

    return x_spline, y_spline, tck

# pylint: disable=line-too-long
def generate_start_stop_line(tck, u, distance_from_middle, length) -> tuple[list[float], list[float], list[float], list[float]]:
    """Generate points for a start-/stop-line. The start-/stop-line
        start at the given distance from the line middle on both
        sides and has a dediacted length.

    Args:
        tck (tuple(t,c,k)): Vector of knots, the B-spline coefficients, and the degree of the spline.
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

# pylint: disable=too-many-arguments, line-too-long, too-many-locals
def generate_track_image(points, image_width, image_height, image_line_width, pixel_per_m, is_debug_mode) -> plt.Figure:
    """Generate the image with the line follower track.

    Args:
        points (list[tuple[float, float]]): List of points.
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

    # Create figure and axis.
    dpi = 72 # Use a dpi of 72 to plot with exact pixel sizes.
    fig, ax = plt.subplots(figsize=(image_width/dpi, image_height/dpi),dpi=dpi)

    # Set background color.
    ax.set_facecolor(background_color)

    # Generate splines through list of points.
    x_spline, y_spline, tck = generate_spline(points)

    # Plot the line.
    ax.plot(x_spline, y_spline, color=line_color, linewidth=image_line_width, zorder=1)

    # Show the points used for generation in debug mode.
    if is_debug_mode is True:

        # Convert the points to separate x- and y-coordinates.
        x_points = [point[0] for point in points]
        y_points = [point[1] for point in points]

        ax.scatter(x_points, y_points, color=line_points_color, linewidth=image_line_width, zorder=2)

    # Plot start- and stop-line
    x_perpendicular_low, y_perpendicular_low, \
    x_perpendicular_high, y_perpendicular_high = \
        generate_start_stop_line(   tck,
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

def get_world_and_image_file_name(user_world_file_name: str) -> tuple[str, str]:
    """Get the file name of the world and image used for the ground.

    Args:
        user_world_file_name (str): The world file name from the user.

    Returns:
        tuple[str, str]: World file name and image file name.
    """
    world_file_name = ""
    image_file_name = ""

    if user_world_file_name.endswith(".wbt") is False:
        world_file_name = user_world_file_name + ".wbt"
        image_file_name = user_world_file_name + ".png"
    else:
        world_file_name = user_world_file_name
        image_file_name = user_world_file_name.replace(".wbt", ".png")

    return (world_file_name, image_file_name)

def create_world_info(title: str, description: str, author: str, author_email: str, basic_time_step: float) -> WorldInfo:
    """Create webots world info node.

    Args:
        title (str): World title.
        description (str): Short world description.
        author (str): Name of the world author.
        author_email (str): EMail address of the world author.
        basic_time_step (float): Basic simulation time step.

    Returns:
        WorldInfo: _description_
    """
    world_creation_date = datetime.today().strftime('%Y-%m-%d')

    world_info = WorldInfo()
    world_info["title"].value = title
    world_info["info"].values = [
        description,
        f"{author} <{author_email}>",
        world_creation_date,
        _get_cmd_line_parameters()
    ]
    world_info["basicTimeStep"].value = basic_time_step

    return world_info

def create_viewpoint(arena_width: float, arena_length: float) -> Viewpoint:
    """Create viewpoint on arena.

    Args:
        arena_width (float): Arena width in m.
        arena_length (float): Arena length in m.

    Returns:
        Viewpoint: Viewpoint node
    """
    viewpoint = Viewpoint()
    viewpoint["orientation"].values = [0, 1, 0, np.pi / 4]
    viewpoint["position"].values = [-2 * arena_width, 0, 2 * arena_length]

    return viewpoint

def create_textured_background() -> Node:
    """Create a textured background for the arena.

    Returns:
        Node: Textured background node.
    """
    return Node("TexturedBackground")

def create_textured_background_light() -> Node:
    """Create a textured background light for the arena.

    Returns:
        Node: Textured background light node.
    """
    return Node("TexturedBackgroundLight")

def create_rectangle_arena(arena_width: float, arena_length: float, image_file_name) -> Node:
    """Create a rectangle arena and use the image as ground.

    Args:
        arena_width (float): Arena width in m.
        arena_length (float): Arena length in m.
        image_file_name (_type_): The name of the image, used on ground.

    Returns:
        Node: Rectangle arena node.
    """
    rectangle_arena = Node("RectangleArena")
    rectangle_arena.add_fields([
        SFVec2f("floorSize", [arena_width, arena_length]),
        SFVec2f("floorTileSize", [arena_width, arena_length]),
        SFNode("floorAppearance", PBRAppearance())
    ])

    rectangle_arena["floorAppearance"].value["baseColorMap"].value = ImageTexture()
    rectangle_arena["floorAppearance"].value["baseColorMap"].value["url"].values = [image_file_name]
    rectangle_arena["floorAppearance"].value["metalness"].value = 0

    return rectangle_arena

def create_contact_properties(material_ground: str, material_robot: str, static_friction: Union[None,float], dynamic_friction: Union[None,float]) -> ContactProperties:
    """Create contact properties for the given materials, considering the
        static and dynamic friction.

    Args:
        material_ground (str): Name of the ground material.
        material_robot (str): Name of the robot contact material.
        static_friction (Union[None,float]): Static friction.
        dynamic_friction (Union[None,float]): Dynamic friction.

    Returns:
        ContactProperties: Contact properties node.
    """
    contact_properties = ContactProperties()
    contact_properties["material1"].value = material_ground
    contact_properties["material2"].value = material_robot

    if static_friction is not None:
        contact_properties["coulombFriction"].values = [static_friction]

    if dynamic_friction is not None:
        contact_properties["forceDependentSlip"].values = [dynamic_friction]

    return contact_properties

def add_friction_to_world(world_info: WorldInfo, material_ground: str, material_robot: str, material_property: str) -> bool:
    """Add friction to a world info node, depended on the materials and their property.

    Args:
        world_info (WorldInfo): World info node.
        material_ground (str): Name of the ground material.
        material_robot (str): Name of the robot contact material.
        material_property (str): The material propertiy, like e.g. dry or wet.

    Returns:
        bool: If successful, it will return True otherwise False.
    """
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
                contact_properties = create_contact_properties(material_ground, material_robot, static_friction, dynamic_friction)
                world_info["contactProperties"].values = [contact_properties]
                status = True

    return status

################################################################################
# Main
################################################################################
