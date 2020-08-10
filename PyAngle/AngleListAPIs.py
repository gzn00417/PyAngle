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

