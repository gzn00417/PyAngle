import math
from fractions import Fraction
from typing import Union

input_t = Union[int, float, str, Fraction]

"""
A simple package for angle calculation
"""


class Angle:
    """Class of Mathematic Angle
    > designed especially for angle in the fmt of DMS(Degree, Minute and Second)
    > immutable object
    `deg` (int): deg of the angle;
    `minute` (int): minute of the angle;
    `sec` (float): sec of the angle;
    """

    _deg: Fraction = Fraction(0)

    def __init__(self, deg: input_t):
        self._deg = Fraction(deg)
        self.adjust()

    @staticmethod
    def from_dms(deg: input_t, minute: input_t = 0, sec: input_t = 0) -> 'Angle':
        """Factory Method for Degree, Minute and Second
        """
        return Angle(Fraction(deg) + Fraction(minute) / 60 + Fraction(sec) / 3600)

    @staticmethod
    def from_degree(deg: input_t) -> 'Angle':
        """Factory Method for ONLY Degree
        """
        return Angle(deg)

    @staticmethod
    def from_radian(rad: input_t) -> 'Angle':
        """Factory Method for Radian
        """
        return Angle(Fraction(math.degrees(Fraction(rad))))

    @staticmethod
    def from_atan2(x: input_t, y: input_t) -> 'Angle':
        """Factory Method for (x, y)
        """
        return Angle.from_radian(math.atan2(Fraction(y), Fraction(x)))

    def adjust(self):
        """Adjust the Format of the Angle, Satisfy: `0 <= d < 360`, `0 <= m, s < 60`
        """
        while self._deg < 0:
            self._deg += 360
        while self._deg >= 360:
            self._deg -= 360

    def deg_i(self) -> int:
        """Get deg in the fmt of DMS
        """
        return int(float(self._deg))

    def min_i(self) -> int:
        """Get minute in the fmt of DMS
        """
        return int((self._deg - Fraction(self.deg_i())) * Fraction(60))

    def sec_f(self) -> float:
        """Get sec in the fmt of DMS
        """
        angle_min = self._deg * 60
        return float((angle_min - int(angle_min)) * 60)

    def __add__(self, other: 'Angle'):
        """(+)Calculate the sum of self and angle
        """
        return Angle(self._deg.__add__(other._deg))

    def __sub__(self, other: 'Angle'):
        """(-)Calculate the difference of self(minuend) and angle(subtrahend)
        """
        return Angle(self._deg.__sub__(other._deg))

    def __mul__(self, n: input_t):
        """(*)Calculate the product of self and angle
        """
        return Angle(self._deg.__mul__(Fraction(n)))

    def __truediv__(self, n: input_t):
        """(/)Calculate the true quotient of self(dividend) and angle(divisor)
        """
        return Angle(self._deg.__truediv__(Fraction(n)))

    def __floordiv__(self, n: input_t):
        """(//)Calculate the floor quotient of self(dividend) and angle(divisor)
        """
        return Angle(self._deg.__floordiv__(Fraction(n)))

    def __mod__(self, other: 'Angle'):
        """(%)Calculate the remainder of self(dividend) and angle(divisor)
        """
        return Angle(self._deg.__mod__(other._deg))

    def __cmp__(self, other: 'Angle'):
        """compare two angles
        -1 if self <  other;
         0 if self == other;
         1 if self >  other;
        """
        return self._deg - other._deg

    def __eq__(self, other: 'Angle'):
        """==
        """
        return self.__cmp__(other) == 0

    def __ne__(self, other: 'Angle'):
        """!=
        """
        return self.__cmp__(other) != 0

    def __le__(self, other: 'Angle'):
        """<=
        """
        return self.__cmp__(other) <= 0

    def __lt__(self, other: 'Angle'):
        """<
        """
        return self.__cmp__(other) < 0

    def __ge__(self, other: 'Angle'):
        """>=
        """
        return self.__cmp__(other) >= 0

    def __gt__(self, other: 'Angle'):
        """>
        """
        return self.__cmp__(other) > 0

    def __str__(self) -> str:
        """Convert angle into string(" " as interval)
        """
        return "{:d} {:d} {:.2f}".format(
            self.deg_i(), self.min_i(), self.sec_f()
        )

    def to_deg(self) -> float:
        """Convert angle into degrees(only deg(float) without minute & sec)
        """
        return float(self._deg)

    def to_rad(self) -> float:
        """Convert angle into radians(float)
        """
        return math.radians(self.to_deg())

    def to_atan2(self, x=None, y=None) -> (float, float):
        """Convert angle into `(x', y')` by `(x, y)`.
        When one of x, y is None, calculate the value of the other one(if not None) that satisfies `y / x = tan`.
        When both of x, y is Nones, returns (x', y') that satisfies `x'^2 + y'^2 = 1`, that is, `x' = cos, y' = sin`
        When both of x, y is not None, return themselves if they are a coordinates of the valid ones, or raise Exception.
        Eg.
        >>> angle = Angle(deg=45)
        >>> angle.to_atan2(x=1.0)
        (1.0, 1.0)
        >>> angle.to_atan2(y=2.0)
        (2.0, 2.0)
        >>> angle.to_atan2()
        (0.707, 0.707)
        """
        # base tan = y / x
        # default: x = cos, y = sin
        if x is None and y is None:
            return self.cos(), self.sin()
        # calculate x by y
        elif x is None:
            return y / self.tan(), y  # x = y / tan
        # calculate y by x
        elif y is None:
            return x, x * self.tan()  # y = x * tan
        # x, y are both not None and valid
        elif math.isclose(y / x, self.tan()):
            return x, y  # return themselves if checked
        raise Exception('Invalid x,y pair!')

    def fmt_str(self, fmt="aaa°bbb′ccc″") -> str:
        """Convert angle into string of fmt(default: `"aaa°bbb′ccc″"`)
        `aaa` is deg, `bbb` is minute, `ccc` is sec, `DDD` is only deg(float),
        `RRR` is radian, `XXX` is horizontal ordinate, `YYY` is vertical ordinate.
        > default: `{:.2f}`
        Eg.
        >>> angle = Angle(45)
        >>> angle.fmt_str()
        2°4′6″
        >>> angle.fmt_str(fmt="aaaDbbbMcccS")
        3D5M7S
        >>> angle.fmt_str(fmt="aaa bbb ccc")
        1 4 9
        >>> angle.fmt_str(fmt="DDDD")
        123D
        >>> angle.fmt_str(fmt="RRRrad")
        1.99rad
        >>> angle.fmt_str(fmt="XXX, YYY")
        0.5, 0.87
        """
        # DMS
        if fmt.find("aaa") >= 0 and fmt.find("bbb") >= 0 and fmt.find("ccc") >= 0:
            return (
                fmt.replace("aaa", str(self.deg_i()), 1)  # deg
                    .replace("bbb", str(self.min_i()), 1)  # minute
                    .replace("ccc", "{:.2f}".format(self.sec_f()), 1)  # sec
            )
        # Degree
        elif fmt.find("DDD") >= 0:
            return fmt.replace("DDD", "{:.2f}".format(self.to_deg()), 1)
        # Radian
        elif fmt.find("RRR") >= 0:
            return fmt.replace("RRR", "{:.2f}".format(self.to_rad()), 1)
        # (x, y)
        elif fmt.find("XXX") >= 0 and fmt.find("YYY") >= 0:
            x_y_pair = self.to_atan2()  # get the tuple of (x, y)
            return fmt.replace("XXX", "{:.2f}".format(x_y_pair[0])).replace(
                "YYY", "{:.2f}".format(x_y_pair[1])
            )
        # TODO raise Exception
        pass

    def sin(self) -> float:
        """sinθ
        """
        return math.sin(self.to_rad())

    def cos(self) -> float:
        """cosθ
        """
        return math.cos(self.to_rad())

    def tan(self) -> float:
        """tanθ
        """
        return math.tan(self.to_rad())

    def isZeroAngle(self) -> bool:
        """Judge if it is zero angle, that is, 0°
        """
        return math.isclose(self.to_deg(), 0)

    def isAcuteAngle(self) -> bool:
        """Judge if it is acute angle(0°, 90°)
        """
        return 0 < self.to_deg() < 90

    def isRightAngle(self) -> bool:
        """Judge if it is right angle, that is, 90°
        """
        return math.isclose(self.to_deg(), 90)

    def isObtuseAngle(self) -> bool:
        """Judge if it is obtuse angle(90°, 180°)
        """
        return 90 < self.to_deg() < 180

    def isMinorAngle(self) -> bool:
        """Judge if it is minor angle(0°, 180°)
        """
        return 0 < self.to_deg() < 180

    def isStraightAngle(self) -> bool:
        """Judge if it is right angle, that is, 180°
        """
        return math.isclose(self.to_deg(), 180)

    def isMajorAngle(self) -> bool:
        """Judge if it is major angle(180°, 360°)
        """
        return 180 < self.to_deg() < 360