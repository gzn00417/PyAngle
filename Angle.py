import math

"""
A simple package for angle calculation
"""


class Angle:
    """Class of Mathematic Angle
    immutable object

    degree (int): degree of the angle;
    minute (int): minute of the angle;
    second (float): second of the angle;
    """

    degree = 0.0
    minute = 0.0
    second = 0.0

    def __init__(self, degree=None, minute=None, second=None, rad=None, x=None, y=None):
        """Creator of Angle
        
        Format Priority:
        1. DMS: degree, minute, second;
        2. Degree: degree;
        3. Rad: rad;
        4. (x, y): x, y

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

    def getDegree(self):
        return int(self.degree)

    def getMinute(self):
        return int(self.minute)

    def getSecond(self):
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
            / n,
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

