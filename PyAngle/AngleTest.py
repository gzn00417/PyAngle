import unittest
from unittest import TestCase
import math

from PyAngle.Angle import *


class AngleTest(TestCase):
    def test_init(self):
        angle1 = Angle.from_dms(deg=1.0, minute=2.0, sec=3.0)
        self.assertEqual(1, angle1.deg_i())
        self.assertEqual(2, angle1.min_i())
        self.assertEqual(3, angle1.sec_f())

        angle2 = Angle(deg=4.3456)
        self.assertEqual(4, angle2.deg_i())
        self.assertAlmostEqual(20, angle2.min_i())
        self.assertNotEqual(0, angle2.sec_f())
        self.assertAlmostEqual(4.3456, angle2.to_deg(), delta=0.01)

        angle3 = Angle.from_radian(rad=1.5708)
        self.assertAlmostEqual(90, angle3.deg_i(), delta=1)
        self.assertAlmostEqual(1.5708, angle3.to_rad(), delta=0.01)

        angle4 = Angle.from_atan2(x=1, y=1)
        self.assertAlmostEqual(45, angle4.deg_i(), delta=1)

    def test_add(self):
        angle1 = Angle.from_dms(deg=100, minute=10, sec=1)
        angle2 = Angle.from_dms(deg=300, minute=30, sec=3)
        angle3 = angle1 + angle2
        self.assertAlmostEqual(40, angle3.deg_i(), delta=1)

    def test_sub(self):
        angle1 = Angle.from_dms(deg=100, minute=10, sec=1)
        angle2 = Angle.from_dms(deg=300, minute=30, sec=3)
        angle3 = angle1 - angle2
        self.assertAlmostEqual(160, angle3.deg_i(), delta=1)

    def test_mul(self):
        angle1 = Angle.from_dms(deg=100, minute=10, sec=1)
        angle2 = angle1 * 6.666
        self.assertAlmostEqual(306.6, angle2.deg_i(), delta=1)

    def test_truediv(self):
        angle1 = Angle.from_dms(deg=100, minute=10, sec=1)
        angle2 = angle1 / 6
        self.assertAlmostEqual(16.6, angle2.deg_i(), delta=1)

    def test_floordiv(self):
        angle1 = Angle.from_dms(deg=100, minute=10, sec=1)
        angle2 = angle1 // 6
        self.assertAlmostEqual(17, angle2.deg_i(), delta=1)

    def test_mod(self):
        angle1 = Angle.from_dms(deg=100, minute=10, sec=1)
        angle2 = Angle.from_dms(deg=330, minute=30, sec=3)
        angle3 = angle2 % angle1
        self.assertAlmostEqual(30, angle3.deg_i(), delta=1)

    def test_str_toString(self):
        angle1 = Angle.from_dms(deg=100, minute=10, sec=1)
        self.assertEqual("100 10 1.00", str(angle1))
        self.assertEqual("100°10′1.00″", angle1.fmt_str())
        self.assertEqual(angle1.fmt_str(fmt="aaaDbbbMcccS"), "100D10M1.00S")
        self.assertEqual(
            "{:.2f}D".format(angle1.to_deg()), angle1.fmt_str(fmt="DDDD")
        )
        self.assertEqual(
            "{:.2f}r".format(angle1.to_rad()), angle1.fmt_str(fmt="RRRr")
        )
        self.assertEqual(
            "({:.2f}, {:.2f})".format(angle1.cos(), angle1.sin()),
            angle1.fmt_str(fmt="(XXX, YYY)")
        )

    def test_cmp(self):
        angle1 = Angle.from_dms(deg=100, minute=10, sec=1)
        angle2 = Angle.from_dms(deg=100, minute=10, sec=0)
        angle3 = Angle.from_dms(deg=100, minute=10, sec=2)
        angle4 = Angle.from_dms(deg=101, minute=9, sec=0)
        angle5 = Angle.from_dms(deg=100, minute=10, sec=1)
        self.assertTrue(angle1 == angle1)
        self.assertTrue(angle1 >= angle2)
        self.assertTrue(angle1 < angle3)
        self.assertTrue(angle4 > angle1)
        self.assertTrue(angle2 <= angle3)
        self.assertTrue(angle1 != angle4)
        self.assertTrue(angle1 == angle5)

    def test_trigonometric_functions(self):
        angle1 = Angle.from_dms(deg=30)
        self.assertAlmostEqual(0.50, angle1.sin(), delta=0.01)
        self.assertAlmostEqual(0.87, angle1.cos(), delta=0.01)
        self.assertAlmostEqual(0.57, angle1.tan(), delta=0.01)

    def test_toXY(self):
        angle1 = Angle.from_dms(deg=30)
        self.assertTupleEqual(
            (math.cos(math.radians(30)), math.sin(math.radians(30))), angle1.to_atan2()
        )
        self.assertTupleEqual((1, math.tan(math.radians(30))), angle1.to_atan2(x=1))
        self.assertTupleEqual((3, math.sqrt(3)), angle1.to_atan2(y=math.sqrt(3)))

    def test_judge_angle_types(self):
        self.assertTrue(Angle.from_dms(deg=0).isZeroAngle())
        self.assertTrue(Angle.from_dms(deg=30).isAcuteAngle())
        self.assertTrue(Angle.from_dms(deg=30).isMinorAngle())
        self.assertFalse(Angle.from_dms(deg=30).isRightAngle())
        self.assertTrue(Angle.from_dms(deg=90).isRightAngle())
        self.assertTrue(Angle.from_dms(deg=100).isObtuseAngle())
        self.assertFalse(Angle.from_dms(deg=100).isRightAngle())
        self.assertFalse(Angle.from_dms(deg=100).isAcuteAngle())
        self.assertFalse(Angle.from_dms(deg=100).isStraightAngle())
        self.assertTrue(Angle.from_dms(deg=180).isStraightAngle())
        self.assertFalse(Angle.from_dms(deg=190).isMinorAngle())
        self.assertTrue(Angle.from_dms(deg=110).isMinorAngle())
        self.assertTrue(Angle.from_dms(deg=200).isMajorAngle())


if __name__ == "__main__":
    unittest.main()