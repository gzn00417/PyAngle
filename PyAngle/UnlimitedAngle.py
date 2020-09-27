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

    def to_Angle(self) -> "Angle":
        """switch `UnlimitedAngle` into `Angle`
        """
        return Angle.from_degrees(degrees=self.to_degrees())
