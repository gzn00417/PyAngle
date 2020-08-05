import unittest
from unittest import TestCase
import math

from PyAngle.Angle import *


class AngleTest(TestCase):
    def test_init(self):
        angle1 = Angle(degree=1.0, minute=2.0, second=3.0)
        self.assertEqual(angle1.getDegree(), 1)
        self.assertEqual(angle1.getMinute(), 2)
        self.assertEqual(angle1.getSecond(), 3.0)

        angle2 = Angle(degree=4.3456)
        self.assertEqual(angle2.getDegree(), 4)
        self.assertAlmostEqual(angle2.getMinute(), 20)
        self.assertNotEqual(angle2.getSecond(), 0)
        self.assertAlmostEqual(angle2.toDegrees(), 4.3456, delta=0.01)

        angle3 = Angle(rad=1.5708)
        self.assertAlmostEqual(angle3.getDegree(), 90, delta=1)
        self.assertAlmostEqual(angle3.toRadians(), 1.5708, delta=0.01)

        angle4 = Angle(x=1, y=1)
        self.assertAlmostEqual(angle4.getDegree(), 45, delta=1)

    def test_add(self):
        angle1 = Angle(degree=100, minute=10, second=1)
        angle2 = Angle(degree=300, minute=30, second=3)
        angle3 = angle1 + angle2
        self.assertAlmostEqual(angle3.getDegree(), 40, delta=1)

    def test_sub(self):
        angle1 = Angle(degree=100, minute=10, second=1)
        angle2 = Angle(degree=300, minute=30, second=3)
        angle3 = angle1 - angle2
        self.assertAlmostEqual(angle3.getDegree(), 160, delta=1)

    def test_mul(self):
        angle1 = Angle(degree=100, minute=10, second=1)
        angle2 = angle1 * 6.666
        self.assertAlmostEqual(angle2.getDegree(), 306.6, delta=1)

    def test_truediv(self):
        angle1 = Angle(degree=100, minute=10, second=1)
        angle2 = angle1 / 6
        self.assertAlmostEqual(angle2.getDegree(), 16.6, delta=1)

    def test_floordiv(self):
        angle1 = Angle(degree=100, minute=10, second=1)
        angle2 = angle1 // 6
        self.assertAlmostEqual(angle2.getDegree(), 17, delta=1)

    def test_mod(self):
        angle1 = Angle(degree=100, minute=10, second=1)
        angle2 = Angle(degree=330, minute=30, second=3)
        angle3 = angle2 % angle1
        self.assertAlmostEqual(angle3.getDegree(), 30, delta=1)

    def test_str_toString(self):
        angle1 = Angle(degree=100, minute=10, second=1)
        self.assertEqual(str(angle1), "100 10 1.00")
        self.assertEqual(angle1.toString(), "100°10′1.00″")
        self.assertEqual(angle1.toString(form="aaaDbbbMcccS"), "100D10M1.00S")
        self.assertEqual(
            angle1.toString(form="DDDD"), "{:.2f}D".format(angle1.toDegrees())
        )
        self.assertEqual(
            angle1.toString(form="RRRr"), "{:.2f}r".format(angle1.toRadians())
        )
        self.assertEqual(
            angle1.toString(form="(XXX, YYY)"),
            "({:.2f}, {:.2f})".format(angle1.cos(), angle1.sin()),
        )

    def test_cmp(self):
        angle1 = Angle(degree=100, minute=10, second=1)
        angle2 = Angle(degree=100, minute=10, second=0)
        angle3 = Angle(degree=100, minute=10, second=2)
        angle4 = Angle(degree=101, minute=9, second=0)
        angle5 = Angle(degree=100, minute=10, second=1)
        self.assertTrue(angle1 == angle1)
        self.assertTrue(angle1 >= angle2)
        self.assertTrue(angle1 < angle3)
        self.assertTrue(angle4 > angle1)
        self.assertTrue(angle2 <= angle3)
        self.assertTrue(angle1 != angle4)
        self.assertTrue(angle1 == angle5)

    def test_trigonometric_functions(self):
        angle1 = Angle(degree=30)
        self.assertAlmostEqual(angle1.sin(), 0.50, delta=0.01)
        self.assertAlmostEqual(angle1.cos(), 0.87, delta=0.01)
        self.assertAlmostEqual(angle1.tan(), 0.57, delta=0.01)

    def test_toXY(self):
        angle1 = Angle(degree=30)
        self.assertTupleEqual(
            angle1.toXY(), (math.cos(math.radians(30)), math.sin(math.radians(30)))
        )
        self.assertTupleEqual(angle1.toXY(x=1), (1, math.tan(math.radians(30))))
        self.assertTupleEqual(angle1.toXY(y=math.sqrt(3)), (3, math.sqrt(3)))

    def test_judge_angle_types(self):
        self.assertTrue(Angle(degree=0).isZeroAngle())
        self.assertTrue(Angle(degree=30).isAcuteAngle())
        self.assertTrue(Angle(degree=30).isMinorAngle())
        self.assertFalse(Angle(degree=30).isRightAngle())
        self.assertTrue(Angle(degree=90).isRightAngle())
        self.assertTrue(Angle(degree=100).isObtuseAngle())
        self.assertFalse(Angle(degree=100).isRightAngle())
        self.assertFalse(Angle(degree=100).isAcuteAngle())
        self.assertFalse(Angle(degree=100).isStraightAngle())
        self.assertTrue(Angle(degree=180).isStraightAngle())
        self.assertFalse(Angle(degree=190).isMinorAngle())
        self.assertTrue(Angle(degree=110).isMinorAngle())
        self.assertTrue(Angle(degree=200).isMajorAngle())


if __name__ == "__main__":
    unittest.main()

