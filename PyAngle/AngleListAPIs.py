"""
APIs for list of Angle
"""

from PyAngle.Angle import *


def from_atan2_list_to_angle_list(angles: [(float, float)]) -> ["Angle"]:
    return [Angle.from_atan2(angle[0], angle[1]) for angle in angles]


def from_degrees_list_to_angle_list(angles: [float]) -> ["Angle"]:
    return [Angle.from_degrees(angle) for angle in angles]


def from_rad_list_to_angle_list(angles: [float]) -> ["Angle"]:
    return [Angle.from_rad(angle) for angle in angles]


def from_angle_list_to_atan2_list(angles: ["Angle"]) -> [(float, float)]:
    return [angle.to_atan2() for angle in angles]


def from_angle_list_to_degrees_list(angles: ["Angle"]) -> [float]:
    return [angle.to_degrees() for angle in angles]


def from_angle_list_to_rad_list(angles: ["Angle"]) -> [float]:
    return [angle.to_rad() for angle in angles]


def get_nearest_angle(angle: "Angle", angles: ["Angle"]) -> "Angle":
    """To get the nearest angle in `angles` with `angle` (return `None` if `angles` is empty)
    """
    nearest_angle = None
    min_gap = Angle.from_degrees(degrees=180)
    for a in angles:
        gap = min(a - angle, angle - a)
        if gap < min_gap:
            min_gap = gap
            nearest_angle = a
    return nearest_angle


def get_furthest_angle(angle: "Angle", angles: ["Angle"]) -> "Angle":
    """To get the furthest angle in `angles` with `angle` (return `None` if `angles` is empty)
    """
    furthest_angle = None
    max_gap = Angle.from_degrees(degrees=0)
    for a in angles:
        gap = min(a - angle, angle - a)
        if gap > max_gap:
            max_gap = gap
            furthest_angle = a
    return furthest_angle
