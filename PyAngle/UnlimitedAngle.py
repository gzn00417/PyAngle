import math
from fractions import Fraction

from PyAngle.Angle import *


class UnlimitedAngle(Angle):
    """Extends from `Angle` whose degrees ranges [-∞, +∞] (without restrict)
    """

    def __init__(self, a: "Angle"):
        super().__init__(a)

    def _Angle__adjust(self):
        """Do not adjust degrees since it's unlimited
        """
        pass

    @staticmethod
    def from_dms(deg: float, min: float = 0, sec: float = 0) -> "UnlimitedAngle":
        """Factory Method for Degree, Minute and Second
        """
        return UnlimitedAngle(Fraction(deg) + Fraction(min) / 60 + Fraction(sec) / 3600)

    @staticmethod
    def from_degrees(degrees: float) -> "UnlimitedAngle":
        """Factory Method for ONLY Degree
        """
        return UnlimitedAngle(degrees)

    @staticmethod
    def from_rad(rad: float) -> "UnlimitedAngle":
        """Factory Method for Radian
        """
        return UnlimitedAngle(Fraction(math.degrees(Fraction(rad))))

    @staticmethod
    def from_atan2(x: float, y: float) -> "UnlimitedAngle":
        """Factory Method for (x, y)
        """
        return UnlimitedAngle.from_rad(math.atan2(Fraction(y), Fraction(x)))

    def to_Angle(self) -> "Angle":
        """switch `UnlimitedAngle` into `Angle`
        """
        return Angle.from_degrees(degrees=self.to_degrees())
