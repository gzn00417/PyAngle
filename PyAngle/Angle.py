import math
from fractions import Fraction


class Angle:
    """Class of Mathematic Angle
    > designed especially for angle in the format of DMS(Degree, Minute and Second)
    > immutable object
    > guarantee `0 <= degrees < 360` 
    `deg` (int): degree of the angle in the format of DMS;
    `min` (int): minute of the angle in the format of DMS;
    `sec` (float): second of the angle in the format of DMS;
    `degrees` (float): degree of the angle in the format of ONLY degree;
    `rad` (float): rad of the angle in the format of radians;
    `atan2` (float, float): (x, y) of the angle in the format of 2D-vector;
    """

    __deg: Fraction = Fraction(0)

    def __init__(self, a: "Angle"):
        self.__deg = Fraction(a.to_degrees() if isinstance(a, Angle) else a)
        self.__adjust()

    @staticmethod
    def from_dms(deg: float, min: float = 0, sec: float = 0) -> "Angle":
        """Factory Method for Degree, Minute and Second
        """
        return Angle(Fraction(deg) + Fraction(min) / 60 + Fraction(sec) / 3600)

    @staticmethod
    def from_degrees(degrees: float) -> "Angle":
        """Factory Method for ONLY Degree
        """
        return Angle(degrees)

    @staticmethod
    def from_rad(rad: float) -> "Angle":
        """Factory Method for Radian
        """
        return Angle(Fraction(math.degrees(Fraction(rad))))

    @staticmethod
    def from_atan2(x: float, y: float) -> "Angle":
        """Factory Method for (x, y)
        """
        return Angle.from_rad(math.atan2(Fraction(y), Fraction(x)))

    def __adjust(self):
        """Adjust the Format of the Angle, Satisfy: `0 <= __deg < 360`
        """
        while self.__deg < 0:
            self.__deg += 360
        while self.__deg >= 360:
            self.__deg -= 360

    def get_deg(self) -> int:
        """Get deg in the fmt of DMS
        """
        return int(float(self.__deg))

    def get_min(self) -> int:
        """Get minute in the fmt of DMS
        """
        return int((self.__deg - Fraction(self.get_deg())) * Fraction(60))

    def get_sec(self) -> float:
        """Get sec in the fmt of DMS
        """
        angle_min = self.__deg * 60
        return float((angle_min - int(angle_min)) * 60)

    def __add__(self, other: "Angle"):
        """(+)Calculate the sum of self and angle
        """
        return self.from_degrees(self.__deg.__add__(other.__deg))

    def __sub__(self, other: "Angle"):
        """(-)Calculate the difference of self(minuend) and angle(subtrahend)
        """
        return self.from_degrees(self.__deg.__sub__(other.__deg))

    def __mul__(self, n: float):
        """(*)Calculate the product of self and angle
        """
        return self.from_degrees(self.__deg.__mul__(Fraction(n)))

    def __truediv__(self, n: float):
        """(/)Calculate the true quotient of self(dividend) and angle(divisor)
        """
        return self.from_degrees(self.__deg.__truediv__(Fraction(n)))

    def __floordiv__(self, n: float):
        """(//)Calculate the floor quotient of self(dividend) and angle(divisor)
        """
        return self.from_degrees(self.__deg.__floordiv__(Fraction(n)))

    def __mod__(self, other: "Angle"):
        """(%)Calculate the remainder of self(dividend) and angle(divisor)
        """
        return self.from_degrees(self.__deg.__mod__(other.__deg))

    def __cmp__(self, other: "Angle"):
        """compare two angles
        negative if self <  other;
        zero     if self == other;
        positive if self >  other;
        """
        return self.__deg - other.__deg

    def __eq__(self, other: "Angle"):
        """==
        """
        return self.__cmp__(other) == 0

    def __ne__(self, other: "Angle"):
        """!=
        """
        return self.__cmp__(other) != 0

    def __le__(self, other: "Angle"):
        """\<=
        """
        return self.__cmp__(other) <= 0

    def __lt__(self, other: "Angle"):
        """\<
        """
        return self.__cmp__(other) < 0

    def __ge__(self, other: "Angle"):
        """\>=
        """
        return self.__cmp__(other) >= 0

    def __gt__(self, other: "Angle"):
        """\>
        """
        return self.__cmp__(other) > 0

    def __str__(self) -> str:
        """Convert angle into string(" " as interval)
        """
        return "{:d} {:d} {:.2f}".format(self.get_deg(), self.get_min(), self.get_sec())

    def __hash__(self) -> int:
        """hash(self)
        """
        return self.__deg.__hash__()

    def to_degrees(self) -> float:
        """Convert angle into degrees(only deg(float) without minute & sec)
        """
        return float(self.__deg)

    def to_rad(self) -> float:
        """Convert angle into radians(float)
        """
        return math.radians(self.to_degrees())

    def to_atan2(self, x: float = None, y: float = None) -> (float, float):
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
        # base: tan = y / x
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
        raise Exception("Invalid x,y pair!")

    def to_fmt_str(self, fmt: str = "aaa°bbb′ccc″", decimal: int = 2) -> str:
        """Convert angle into string of fmt
        `aaa` is deg(int), `bbb` is minute(int), `ccc` is sec(float), `DDD` is only deg(float),
        `RRR` is radian(float), `XXX` is horizontal ordinate(float), `YYY` is vertical ordinate(float).
        > default: fmt = "aaa°bbb′ccc″"`, decimal = 2
        Eg.
        >>> angle = Angle(45)
        >>> angle.to_fmt_str()
        2°4′6″
        >>> angle.to_fmt_str(fmt="aaaDbbbMcccS")
        3D5M7S
        >>> angle.to_fmt_str(fmt="aaa bbb ccc")
        1 4 9
        >>> angle.to_fmt_str(fmt="DDDD")
        123D
        >>> angle.to_fmt_str(fmt="RRRrad")
        1.99rad
        >>> angle.to_fmt_str(fmt="XXX, YYY")
        0.5, 0.87
        """
        # DMS
        if fmt.find("aaa") >= 0 and fmt.find("bbb") >= 0 and fmt.find("ccc") >= 0:
            return (
                fmt.replace("aaa", str(self.get_deg()), 1)  # deg
                .replace("bbb", str(self.get_min()), 1)  # minute
                .replace("ccc", ("{:.%df}" % decimal).format(self.get_sec()), 1)  # sec
            )
        # Degree
        elif fmt.find("DDD") >= 0:
            return fmt.replace(
                "DDD", ("{:.%df}" % decimal).format(self.to_degrees()), 1
            )
        # Radian
        elif fmt.find("RRR") >= 0:
            return fmt.replace("RRR", ("{:.%df}" % decimal).format(self.to_rad()), 1)
        # (x, y)
        elif fmt.find("XXX") >= 0 and fmt.find("YYY") >= 0:
            x_y_pair = self.to_atan2()  # get the tuple of (x, y)
            return fmt.replace(
                "XXX", ("{:.%df}" % decimal).format(x_y_pair[0])
            ).replace("YYY", ("{:.%df}" % decimal).format(x_y_pair[1]))
        raise Exception("Invalid fmt!")

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

    def is_zero_angle(self) -> bool:
        """Judge if it is zero angle, that is, 0°
        """
        return math.isclose(self.to_degrees(), 0)

    def is_acute_angle(self) -> bool:
        """Judge if it is acute angle(0°, 90°)
        """
        return 0 < self.to_degrees() < 90

    def is_right_angle(self) -> bool:
        """Judge if it is right angle, that is, 90°
        """
        return math.isclose(self.to_degrees(), 90)

    def is_obtuse_angle(self) -> bool:
        """Judge if it is obtuse angle(90°, 180°)
        """
        return 90 < self.to_degrees() < 180

    def is_minor_angle(self) -> bool:
        """Judge if it is minor angle(0°, 180°)
        """
        return 0 < self.to_degrees() < 180

    def is_straight_angle(self) -> bool:
        """Judge if it is right angle, that is, 180°
        """
        return math.isclose(self.to_degrees(), 180)

    def is_major_angle(self) -> bool:
        """Judge if it is major angle(180°, 360°)
        """
        return 180 < self.to_degrees() < 360

    def is_complementary_angle_with(self, other: "Angle") -> bool:
        """Judge if they are complementary angles
        """
        return math.isclose((self + other).to_degrees(), 90)

    def is_supplementary_angle_with(self, other: "Angle") -> bool:
        """Judge if they are supplementary angles
        """
        return math.isclose((self + other).to_degrees(), 180)
