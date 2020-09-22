import unittest
from unittest import TestCase
import math

from PyAngle import *


class AngleTest(TestCase):
    def test_init(self):
        angle1 = Angle.from_dms(deg=1.0, min=2.0, sec=3.0)
        self.assertEqual(1, angle1.get_deg())
        self.assertEqual(2, angle1.get_min())
        self.assertEqual(3, angle1.get_sec())

        angle2 = Angle.from_degrees(degrees=4.3456)
        self.assertEqual(4, angle2.get_deg())
        self.assertAlmostEqual(20, angle2.get_min())
        self.assertNotEqual(0, angle2.get_sec())
        self.assertAlmostEqual(4.3456, angle2.to_degrees(), delta=0.01)

        angle3 = Angle.from_rad(rad=1.5708)
        self.assertAlmostEqual(90, angle3.get_deg(), delta=1)
        self.assertAlmostEqual(1.5708, angle3.to_rad(), delta=0.01)

        angle4 = Angle.from_atan2(x=1, y=1)
        self.assertAlmostEqual(45, angle4.get_deg(), delta=1)

        angle5 = Angle.from_degrees(degrees=1000)
        self.assertEqual(280, angle5.to_degrees())

        angle6 = Angle.from_degrees(degrees=-1000)
        self.assertEqual(80, angle6.to_degrees())

        angle7 = Angle(angle6)
        self.assertEqual(80, angle7.to_degrees())

        angle8 = Angle(UnlimitedAngle.from_degrees(degrees=1000))
        self.assertEqual(280, angle8.to_degrees())

    def test_add(self):
        angle1 = Angle.from_dms(deg=100, min=10, sec=1)
        angle2 = Angle.from_dms(deg=300, min=30, sec=3)
        angle3 = angle1 + angle2
        self.assertAlmostEqual(40, angle3.get_deg(), delta=1)

    def test_sub(self):
        angle1 = Angle.from_dms(deg=100, min=10, sec=1)
        angle2 = Angle.from_dms(deg=300, min=30, sec=3)
        angle3 = angle1 - angle2
        self.assertAlmostEqual(160, angle3.get_deg(), delta=1)

    def test_mul(self):
        angle1 = Angle.from_dms(deg=100, min=10, sec=1)
        angle2 = angle1 * 6.666
        self.assertAlmostEqual(306.6, angle2.get_deg(), delta=1)

    def test_truediv(self):
        angle1 = Angle.from_dms(deg=100, min=10, sec=1)
        angle2 = angle1 / 6
        self.assertAlmostEqual(16.6, angle2.get_deg(), delta=1)

    def test_floordiv(self):
        angle1 = Angle.from_dms(deg=100, min=10, sec=1)
        angle2 = angle1 // 6
        self.assertAlmostEqual(17, angle2.get_deg(), delta=1)

    def test_mod(self):
        angle1 = Angle.from_dms(deg=100, min=10, sec=1)
        angle2 = Angle.from_dms(deg=330, min=30, sec=3)
        angle3 = angle2 % angle1
        self.assertAlmostEqual(30, angle3.get_deg(), delta=1)

    def test_str_to_fmt_str(self):
        angle1 = Angle.from_dms(deg=100, min=10, sec=1)
        self.assertEqual("100 10 1.00", str(angle1))
        self.assertEqual("100°10′1.00″", angle1.to_fmt_str())
        self.assertEqual(angle1.to_fmt_str(fmt="aaaDbbbMcccS"), "100D10M1.00S")
        self.assertEqual(
            "{:.2f}D".format(angle1.to_degrees()), angle1.to_fmt_str(fmt="DDDD")
        )
        self.assertEqual(
            "{:.4f}r".format(angle1.to_rad()), angle1.to_fmt_str(fmt="RRRr", decimal=4)
        )
        self.assertEqual(
            "({:.3f}, {:.3f})".format(angle1.cos(), angle1.sin()),
            angle1.to_fmt_str(fmt="(XXX, YYY)", decimal=3),
        )

    def test_cmp(self):
        angle1 = Angle.from_dms(deg=100, min=10, sec=1)
        angle2 = Angle.from_dms(deg=100, min=10, sec=0)
        angle3 = Angle.from_dms(deg=100, min=10, sec=2)
        angle4 = Angle.from_dms(deg=101, min=9, sec=0)
        angle5 = Angle.from_dms(deg=100, min=10, sec=1)
        self.assertTrue(angle1 == angle1)
        self.assertTrue(angle1 >= angle2)
        self.assertTrue(angle1 < angle3)
        self.assertTrue(angle4 > angle1)
        self.assertTrue(angle2 <= angle3)
        self.assertTrue(angle1 != angle4)
        self.assertTrue(angle1 == angle5)
        self.assertEqual(angle1, max(angle1, angle2))
        self.assertEqual(angle3, min(angle3, angle4))
        list1 = [angle2, angle1, angle3, angle4]
        list2 = list1
        list2.sort()
        self.assertListEqual(list1, list2)
        list2 = list1
        list2.sort(reverse=True)
        list1.reverse()
        self.assertListEqual(list1, list2)

    def test_trigonometric_functions(self):
        angle1 = Angle.from_dms(deg=30)
        self.assertAlmostEqual(0.50, angle1.sin(), delta=0.01)
        self.assertAlmostEqual(0.87, angle1.cos(), delta=0.01)
        self.assertAlmostEqual(0.57, angle1.tan(), delta=0.01)

    def test_to_atan2(self):
        angle1 = Angle.from_dms(deg=30)
        self.assertTupleEqual(
            (math.cos(math.radians(30)), math.sin(math.radians(30))), angle1.to_atan2()
        )
        self.assertTupleEqual((1, math.tan(math.radians(30))), angle1.to_atan2(x=1))
        self.assertTupleEqual((3, math.sqrt(3)), angle1.to_atan2(y=math.sqrt(3)))

    def test_judge_angle_types(self):
        self.assertTrue(Angle.from_dms(deg=0).is_zero_angle())
        self.assertTrue(Angle.from_dms(deg=30).is_acute_angle())
        self.assertTrue(Angle.from_dms(deg=30).is_minor_angle())
        self.assertFalse(Angle.from_dms(deg=30).is_right_angle())
        self.assertTrue(Angle.from_dms(deg=90).is_right_angle())
        self.assertTrue(Angle.from_dms(deg=100).is_obtuse_angle())
        self.assertFalse(Angle.from_dms(deg=100).is_right_angle())
        self.assertFalse(Angle.from_dms(deg=100).is_acute_angle())
        self.assertFalse(Angle.from_dms(deg=100).is_straight_angle())
        self.assertTrue(Angle.from_dms(deg=180).is_straight_angle())
        self.assertFalse(Angle.from_dms(deg=190).is_minor_angle())
        self.assertTrue(Angle.from_dms(deg=110).is_minor_angle())
        self.assertTrue(Angle.from_dms(deg=200).is_major_angle())
        self.assertTrue(
            Angle.from_dms(deg=30).is_complementary_angle_with(Angle.from_dms(deg=60))
        )
        self.assertTrue(
            Angle.from_dms(deg=60).is_supplementary_angle_with(Angle.from_dms(deg=120))
        )


if __name__ == "__main__":
    unittest.main()
