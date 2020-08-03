import math

"""
A simple package for angle calculation
"""


class Angle:
    """Class of Mathematic Angle\n
    > immutable object\n
    degree (int): degree of the angle;\n
    minute (int): minute of the angle;\n
    second (float): second of the angle;\n
    """

    degree = 0.0
    minute = 0.0
    second = 0.0

    def __init__(self, degree=None, minute=None, second=None, rad=None, x=None, y=None):
        """Creator of Angle\n
        Format Priority:
        1. DMS: degree, minute, second;\n
        2. Degree: degree;\n
        3. Rad: rad;\n
        4. (x, y): x, y\n
        """
        if degree is not None and minute is not None and second is not None:
            self.createByDMS(d=degree, m=minute, s=second)
        elif degree is not None:
            self.createByDegree(degree=degree)
        elif rad is not None:
            self.createByRadian(rad=rad)
        elif x is not None and y is not None:
            self.createByXY(x=x, y=y)
        else:
            raise GeneratorExit
        self.adjust()

    def createByDMS(self, d, m=0.0, s=0.0):
        self.degree = float(d)
        self.minute = float(m)
        self.second = float(s)

    def createByDegree(self, degree):
        self.createByDMS(d=degree)

    def createByRadian(self, rad):
        self.createByDegree(degree=math.degrees(rad))

    def createByXY(self, x, y):
        self.createByRadian(rad=math.atan2(y, x))

    def adjust(self):
        """Adjust the Format of the Angle, Satisfy: 0 <= d < 360, 0 <= m, s < 60
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
        """(/)Calculate the true quotient of self and angle
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
        """(//)Calculate the floor quotient of self and angle
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
        """(%)Calculate the remainder of self and angle
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

    def __str__(self):
        """Convert angle into string(" " as interval)
        """
        return "{:d} {:d} {:.2f}".format(
            self.getDegree(), self.getMinute(), self.getSecond()
        )

    def toDegrees(self):
        """Convert angle into degrees(only degree(float) without minute & second)
        """
        return float(
            1.0 * self.getDegree()
            + self.getMinute() / 60.0
            + self.getSecond() / 60.0 / 60.0
        )

    def toRadians(self):
        """Convert angle into radians(float)
        """
        return math.radians(self.toDegrees())

    def toString(self, form="aaa°bbb′ccc″"):
        """Convert angle into string of form(default: `"aaa°bbb′ccc″"`)\n
        `aaa` is degree, `bbb` is minute, `ccc` is second, `DDD` is only degree(float),
        `RRR` is radian, `XXX` is horizontal ordinate, `YYY` is vertical ordinate.\n
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
        1.999rad
        >>> angle.toString(form="XXX, YYY")
        0.5, 0.87
        """
        if form.find("aaa") >= 0 and form.find("bbb") >= 0 and form.find("ccc") >= 0:
            return (
                form.replace("aaa", str(self.getDegree()), 1)
                .replace("bbb", str(self.getMinute()), 1)
                .replace("ccc", "{:.2f}".format(self.getSecond()), 1)
            )
        elif form.find("DDD") >= 0:
            return form.replace("DDD", "{:.2f}".format(self.toDegrees()), 1)
        elif form.find("RRR") >= 0:
            return form.replace("RRR", "{:.2f}".format(self.toRadians()), 1)
        elif form.find("XXX") >= 0 and form.find("YYY") >= 0:
            # TODO
            pass
        else:
            # TODO
            raise Exception
