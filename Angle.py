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

    DEGREE_MINUTE_SECOND = "DEGREE_MINUTE_SECOND"
    DEGREE = "DEGREE"
    RADIAN = "RADIAN"
    XY = "XY"

    def __init__(self, form, degree=0.0, minute=0.0, second=0.0, rad=0.0, x=0.0, y=0.0):
        """Creator of Angle
        
        Args:
            degree (float): degree of the angle;
            minute (float): minute of the angle;
            second (float): second of the angle;
            rad (float): Radian of the Angle;
            x (float): horizontal ordinate;
            y (float): vertical ordinate;
            
        """
        if self.DEGREE_MINUTE_SECOND == form:
            self.createByDMS(d=degree, m=minute, s=second)
        elif self.DEGREE == form:
            self.createByDegree(degree=degree)
        elif self.RADIAN == form:
            self.createByRadian(rad=rad)
        elif self.XY == form:
            self.createByXY(x=x, y=y)
        self.adjust()

    def createByDMS(self, d, m=0.0, s=0.0):
        self.degree = float(d)
        self.minute = float(m)
        self.second = float(s)
        self.adjust()

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
            form=self.DEGREE_MINUTE_SECOND,
            degree=self.getDegree() + other.getDegree(),
            minute=self.getMinute() + other.getMinute(),
            second=self.getSecond() + other.getSecond(),
        )

    def __sub__(self, other):
        """(-)Calculate the difference of self(minuend) and angle(subtrahend)
        """
        return Angle(
            form=self.DEGREE_MINUTE_SECOND,
            degree=self.getDegree() - other.getDegree(),
            minute=self.getMinute() - other.getMinute(),
            second=self.getSecond() - other.getSecond(),
        )

    def __mul__(self, n):
        """(×)Calculate the product of self and angle
        """
        return Angle(
            form=self.DEGREE_MINUTE_SECOND,
            degree=0,
            minute=0,
            second=float(self.degree * 60 * 60 + self.minute * 60 + self.second) * n,
        )

    def __truediv__(self, n):
        """(/)Calculate the true quotient of self and angle
        """
        return Angle(
            form=self.DEGREE_MINUTE_SECOND,
            degree=0,
            minute=0,
            second=float(self.degree * 60 * 60 + self.minute * 60 + self.second) / n,
        )

    def __floordiv__(self, n):
        """(//)Calculate the floor quotient of self and angle
        """
        return Angle(
            form=self.DEGREE_MINUTE_SECOND,
            degree=0,
            minute=0,
            second=float(self.degree * 60 * 60 + self.minute * 60 + self.second) / n,
        )

    def __mod__(self, other):
        """(%)Calculate the remainder of self and angle
        """
        return Angle(
            form=self.DEGREE_MINUTE_SECOND,
            degree=0,
            minute=0,
            second=float(self.degree * 60 * 60 + self.minute * 60 + self.second)
            % float(
                other.getDegree() * 60 * 60 + other.getMinute() * 60 + other.getSecond()
            ),
        )

