import math

"""
A simple package for angle calculation
"""


class Angle:
    """Class of Mathematic Angle\n
    > designed especially for angle in the form of DMS(Degree, Minute and Second)\n
    > immutable object\n
    `degree` (int): degree of the angle;\n
    `minute` (int): minute of the angle;\n
    `second` (float): second of the angle;\n
    """

    degree = 0.0  # degree(int when output)
    minute = 0.0  # minute(int when output)
    second = 0.0  # second(float, default: "{:.2f}")

    __DELTA = 0.0001  # const, floats equal difference limit

    def __init__(self, degree=None, minute=None, second=None, rad=None, x=None, y=None):
        """Creator of Angle\n
        Format Priority:\n
        1. DMS: degree, minute, second;\n
        2. Degree: degree;\n
        3. Rad: rad;\n
        4. (x, y): x, y\n
        """
        # DMS
        if degree is not None and minute is not None and second is not None:
            self.__createByDMS(d=degree, m=minute, s=second)
        # Degree
        elif degree is not None:
            self.__createByDegree(degree=degree)
        # Radian
        elif rad is not None:
            self.__createByRadian(rad=rad)
        # (x, y)
        elif x is not None and y is not None:
            self.__createByXY(x=x, y=y)
        # invalid params
        else:
            # TODO: raise Exception
            raise GeneratorExit
        self.adjust()

    def __createByDMS(self, d, m=0.0, s=0.0):
        """Private Initiator For Degree, Minute and Second
        """
        self.degree = float(d)
        self.minute = float(m)
        self.second = float(s)

    def __createByDegree(self, degree):
        """Private Initiator For ONLY Degree
        """
        self.__createByDMS(d=degree)

    def __createByRadian(self, rad):
        """Private Initiator For Radian
        """
        self.__createByDegree(degree=math.degrees(rad))

    def __createByXY(self, x, y):
        """Private Initiator For (x, y)
        """
        self.__createByRadian(rad=math.atan2(y, x))

    def adjust(self):
        """Adjust the Format of the Angle, Satisfy: `0 <= d < 360`, `0 <= m, s < 60`
        """
        self.second += self.degree * 60 * 60 + self.minute * 60
        self.minute = self.degree = 0
        # Satisfy 0 <= s < 60
        self.minute += self.second // 60
        self.second %= 60
        # Satisfy 0 <= m < 60
        self.degree += self.minute // 60
        self.minute %= 60
        # Satisfy 0 <= d < 360
        self.degree %= 360

    def getDegree(self) -> (int):
        """Get degree in the form of DMS
        """
        return int(self.degree)

    def getMinute(self) -> (int):
        """Get minute in the form of DMS
        """
        return int(self.minute)

    def getSecond(self) -> (float):
        """Get second in the form of DMS
        """
        return float(self.second)

    def __add__(self, other):
        """(+)Calculate the sum of self and angle
        """
        return Angle(
            degree=self.getDegree() + other.getDegree(),
            minute=self.getMinute() + other.getMinute(),
            second=self.getSecond() + other.getSecond(),
        )

    def __sub__(self, other):
        """(-)Calculate the difference of self(minuend) and angle(subtrahend)
        """
        return Angle(
            degree=self.getDegree() - other.getDegree(),
            minute=self.getMinute() - other.getMinute(),
            second=self.getSecond() - other.getSecond(),
        )

    def __mul__(self, n):
        """(*)Calculate the product of self and angle
        """
        return Angle(
            degree=0,
            minute=0,
            second=float(
                self.getDegree() * 60 * 60 + self.getMinute() * 60 + self.getSecond()
            )
            * n,
        )

    def __truediv__(self, n):
        """(/)Calculate the true quotient of self(dividend) and angle(divisor)
        """
        return Angle(
            degree=0,
            minute=0,
            second=float(
                self.getDegree() * 60 * 60 + self.getMinute() * 60 + self.getSecond()
            )
            / n,
        )

    def __floordiv__(self, n):
        """(//)Calculate the floor quotient of self(dividend) and angle(divisor)
        """
        return Angle(
            degree=0,
            minute=0,
            second=float(
                self.getDegree() * 60 * 60 + self.getMinute() * 60 + self.getSecond()
            )
            // n,
        )

    def __mod__(self, other):
        """(%)Calculate the remainder of self(dividend) and angle(divisor)
        """
        return Angle(
            degree=0,
            minute=0,
            second=float(
                self.getDegree() * 60 * 60 + self.getMinute() * 60 + self.getSecond()
            )
            % float(
                other.getDegree() * 60 * 60 + other.getMinute() * 60 + other.getSecond()
            ),
        )

    def __cmp__(self, other) -> (int):
        """compare two angles\n
        -1 if self <  other;\n
        0  if self == other;\n
        1  if self >  other;
        """
        if self.getDegree() > other.getDegree():
            return 1
        elif self.getDegree() < other.getDegree():
            return -1
        else:
            # degrees are equal
            if self.getMinute() > other.getMinute():
                return 1
            elif self.getMinute() < other.getMinute():
                return -1
            else:
                # degrees and minutes are equal
                if self.getSecond() - other.getSecond() > self.__DELTA:
                    return 1  # self > other
                elif other.getSecond() - self.getSecond() > self.__DELTA:
                    return -1  # self < other
        # all are equal
        return 0

    def __eq__(self, other) -> (bool):
        """==
        """
        return self.__cmp__(other) == 0

    def __ne__(self, other) -> (bool):
        """!=
        """
        return self.__cmp__(other) != 0

    def __le__(self, other) -> (bool):
        """\<=
        """
        return self.__cmp__(other) < 1  # 0, -1s

    def __lt__(self, other) -> (bool):
        """\<
        """
        return self.__cmp__(other) == -1

    def __ge__(self, other) -> (bool):
        """\>=
        """
        return self.__cmp__(other) > -1  # 0, 1

    def __gt__(self, other) -> (bool):
        """\>
        """
        return self.__cmp__(other) == 1

    def __str__(self) -> (str):
        """Convert angle into string(" " as interval)
        """
        return "{:d} {:d} {:.2f}".format(
            self.getDegree(), self.getMinute(), self.getSecond()
        )

    def toDegrees(self) -> (float):
        """Convert angle into degrees(only degree(float) without minute & second)
        """
        return float(
            1.0 * self.getDegree()
            + self.getMinute() / 60.0
            + self.getSecond() / 60.0 / 60.0
        )

    def toRadians(self) -> (float):
        """Convert angle into radians(float)
        """
        return math.radians(self.toDegrees())

    def toString(self, form="aaa°bbb′ccc″") -> (str):
        """Convert angle into string of form(default: `"aaa°bbb′ccc″"`)\n
        `aaa` is degree, `bbb` is minute, `ccc` is second, `DDD` is only degree(float),
        `RRR` is radian, `XXX` is horizontal ordinate, `YYY` is vertical ordinate.\n
        > default: `{:.2f}`\n
        Eg.\n
        >>> angle.toString()
        2°4′6″
        >>> angle.toString(form="aaaDbbbMcccS")
        3D5M7S
        >>> angle.toString(form="aaa bbb ccc")
        1 4 9
        >>> angle.toString(form="DDDD")
        123D
        >>> angle.toString(form="RRRrad")
        1.99rad
        >>> angle.toString(form="XXX, YYY")
        0.5, 0.87
        """
        # DMS
        if form.find("aaa") >= 0 and form.find("bbb") >= 0 and form.find("ccc") >= 0:
            return (
                form.replace("aaa", str(self.getDegree()), 1)  # degree
                .replace("bbb", str(self.getMinute()), 1)  # minute
                .replace("ccc", "{:.2f}".format(self.getSecond()), 1)  # second
            )
        # Degree
        elif form.find("DDD") >= 0:
            return form.replace("DDD", "{:.2f}".format(self.toDegrees()), 1)
        # Radian
        elif form.find("RRR") >= 0:
            return form.replace("RRR", "{:.2f}".format(self.toRadians()), 1)
        # (x, y)
        elif form.find("XXX") >= 0 and form.find("YYY") >= 0:
            tupleXY = self.toXY()  # get the tuple of (x, y)
            return form.replace("XXX", "{:.2f}".format(tupleXY[0])).replace(
                "YYY", "{:.2f}".format(tupleXY[1])
            )
        # TODO raise Exception
        pass

    def sin(self) -> (float):
        """sinθ
        """
        return math.sin(self.toRadians())

    def cos(self) -> (float):
        """cosθ
        """
        return math.cos(self.toRadians())

    def tan(self) -> (float):
        """tanθ
        """
        return math.tan(self.toRadians())

    def toXY(self, x=None, y=None) -> (float, float):
        """Convert angle into `(x', y')` by `(x, y)`.\n
        When one of x, y is None, calculate the value of the other one(if not None) that satisfies `y / x = tan`.\n
        When both of x, y is Nones, returns (x', y') that satisfies `x'^2 + y'^2 = 1`, that is, `x' = cos, y' = sin`\n
        When both of x, y is not None, return themselves if they are a coordinates of the valid ones, or raise Exception.\n
        Eg.\n
        >>> angle = Angle(degree=45)
        >>> angle.toXY(x=1.0)
        (1.0, 1.0)
        >>> angle.toXY(y=2.0)
        (2.0, 2.0)
        >>> angle.toXY()
        (0.707, 0.707)
        """
        # base tan = y / x
        # default: x = cos, y = sin
        if x is None and y is None:
            return (self.cos(), self.sin())
        # calculate x by y
        elif x is None:
            return (y / self.tan(), y)  # x = y / tan
        # calculate y by x
        elif y is None:
            return (x, x * self.tan())  # y = x * tan
        # x, y are both not None and valid
        elif abs(y / x - self.tan()) < self.__DELTA:  # y / x == tan
            return (x, y)  # return themselves if checked
        # TODO: raise Exception
        return (None, None)

