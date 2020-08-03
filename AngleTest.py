import unittest
from unittest import TestCase

from Angle import *


class AngleTest(TestCase):
    def test_init(self):
        angle1 = Angle(
            form=Angle.DEGREE_MINUTE_SECOND, degree=1.0, minute=2.0, second=3.0
        )
        self.assertEqual(angle1.getDegree(), 1)
        self.assertEqual(angle1.getMinute(), 2)
        self.assertEqual(angle1.getSecond(), 3.0)

        angle2 = Angle(form=Angle.DEGREE, degree=4.3456)
        self.assertEqual(angle2.getDegree(), 4)
        self.assertAlmostEqual(angle2.getMinute(), 20)
        self.assertNotEqual(angle2.getSecond(), 0)

        angle3 = Angle(form=Angle.RADIAN, rad=1.5708)
        self.assertAlmostEqual(angle3.getDegree(), 90, delta=1)

        angle4 = Angle(form=Angle.XY, x=1, y=1)
        self.assertAlmostEqual(angle4.getDegree(), 45, delta=1)

    def test_add(self):
        angle1 = Angle(form=Angle.DEGREE_MINUTE_SECOND, degree=100, minute=10, second=1)
        angle2 = Angle(form=Angle.DEGREE_MINUTE_SECOND, degree=300, minute=30, second=3)
        angle3 = angle1 + angle2
        self.assertAlmostEqual(angle3.getDegree(), 40, delta=1)

    def test_sub(self):
        angle1 = Angle(form=Angle.DEGREE_MINUTE_SECOND, degree=100, minute=10, second=1)
        angle2 = Angle(form=Angle.DEGREE_MINUTE_SECOND, degree=300, minute=30, second=3)
        angle3 = angle1 - angle2
        self.assertAlmostEqual(angle3.getDegree(), 160, delta=1)

    def test_mul(self):
        angle1 = Angle(form=Angle.DEGREE_MINUTE_SECOND, degree=100, minute=10, second=1)
        angle2 = angle1 * 6.666
        self.assertAlmostEqual(angle2.getDegree(), 306.6, delta=1)

    def test_truediv(self):
        angle1 = Angle(form=Angle.DEGREE_MINUTE_SECOND, degree=100, minute=10, second=1)
        angle2 = angle1 / 6
        self.assertAlmostEqual(angle2.getDegree(), 16.6, delta=1)

    def test_floordiv(self):
        angle1 = Angle(form=Angle.DEGREE_MINUTE_SECOND, degree=100, minute=10, second=1)
        angle2 = angle1 // 6
        self.assertAlmostEqual(angle2.getDegree(), 16, delta=1)

    def test_mod(self):
        angle1 = Angle(form=Angle.DEGREE_MINUTE_SECOND, degree=100, minute=10, second=1)
        angle2 = Angle(form=Angle.DEGREE_MINUTE_SECOND, degree=330, minute=30, second=3)
        angle3 = angle2 % angle1
        self.assertAlmostEqual(angle3.getDegree(), 30, delta=1)


if __name__ == "__main__":
    unittest.main()

