import unittest
from unittest import TestCase
import math

from PyAngle.Angle import *
from PyAngle.AngleListAPIs import *


class AngleListAPIsTest(TestCase):
    def test_from_angle_list_to_xxx(self):
        angle1 = Angle.from_dms(deg=1, min=2, sec=3)
        angle2 = Angle.from_dms(deg=10, min=20, sec=30)
        angle3 = Angle.from_dms(deg=100, min=2, sec=3)
        self.assertListEqual(
            [angle1.to_atan2(), angle2.to_atan2(), angle3.to_atan2()],
            from_angle_list_to_atan2_list([angle1, angle2, angle3]),
        )
        self.assertListEqual(
            [angle1.to_degrees(), angle2.to_degrees(), angle3.to_degrees()],
            from_angle_list_to_degrees_list([angle1, angle2, angle3]),
        )
        self.assertListEqual(
            [angle1.to_rad(), angle2.to_rad(), angle3.to_rad()],
            from_angle_list_to_rad_list([angle1, angle2, angle3]),
        )

    def test_from_xxx_to_angle_list(self):
        xy1 = (0.234, 0.567)
        xy2 = (0.432, 0.765)
        xy3 = (0.567, 0.789)
        self.assertListEqual(
            [
                Angle.from_atan2(xy1[0], xy1[1]),
                Angle.from_atan2(xy2[0], xy2[1]),
                Angle.from_atan2(xy3[0], xy3[1]),
            ],
            from_atan2_list_to_angle_list([xy1, xy2, xy3]),
        )
        d1 = 1.23
        d2 = 4.56
        d3 = 7.89
        self.assertListEqual(
            [Angle.from_degrees(d1), Angle.from_degrees(d2), Angle.from_degrees(d3)],
            from_degrees_list_to_angle_list([d1, d2, d3]),
        )
        r1 = 0.123
        r2 = 0.456
        r3 = 0.789
        self.assertListEqual(
            [Angle.from_rad(r1), Angle.from_rad(r2), Angle.from_rad(r3)],
            from_rad_list_to_angle_list([r1, r2, r3]),
        )

    def test_get_nearest_or_furthest_angle(self):
        angle1 = Angle.from_degrees(degrees=1)
        angle2 = Angle.from_degrees(degrees=5)
        angle3 = Angle.from_degrees(degrees=10)
        angle4 = Angle.from_degrees(degrees=100)
        angle5 = Angle.from_degrees(degrees=181)
        angle6 = Angle.from_degrees(degrees=270)
        angle7 = Angle.from_degrees(degrees=359)
        # get_nearest_angle
        self.assertIsNone(get_nearest_angle(angle1, []))
        self.assertEqual(angle2, get_nearest_angle(angle1, [angle2, angle3]))
        self.assertEqual(
            angle7,
            get_nearest_angle(angle1, [angle2, angle3, angle4, angle5, angle6, angle7]),
        )
        self.assertEqual(
            angle3, get_nearest_angle(angle2, [angle3, angle4, angle5, angle6, angle7])
        )
        # get_furthest_angle
        self.assertIsNone(get_furthest_angle(angle1, []))
        self.assertEqual(angle3, get_furthest_angle(angle1, [angle2, angle3]))
        self.assertEqual(
            angle5,
            get_furthest_angle(
                angle1, [angle2, angle3, angle4, angle5, angle6, angle7]
            ),
        )
        self.assertEqual(
            angle6,
            get_furthest_angle(
                angle4, [angle1, angle2, angle3, angle4, angle5, angle6, angle7]
            ),
        )


if __name__ == "__main__":
    unittest.main()
