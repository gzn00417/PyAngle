import unittest
from unittest import TestCase
import math

from PyAngle import *


class UnlimitedAngleTest(TestCase):
    def test_init(self):
        ua1 = UnlimitedAngle.from_degrees(degrees=1000)
        self.assertEqual(1000, ua1.to_degrees())
        ua2 = UnlimitedAngle.from_degrees(degrees=-1000)
        self.assertEqual(-1000, ua2.to_degrees())
        ua3 = UnlimitedAngle(Angle(UnlimitedAngle.from_degrees(degrees=1000)))
        self.assertEqual(1280, (ua1 + ua3).to_degrees())

    def test_to_Angle(self):
        a1 = UnlimitedAngle.from_degrees(degrees=1000).to_Angle()
        self.assertEqual(280, a1.to_degrees())
        self.assertEqual(Angle, a1.__class__)
        a2 = UnlimitedAngle.from_degrees(degrees=-1000).to_Angle()
        self.assertEqual(80, a2.to_degrees())
        self.assertEqual(Angle, a2.__class__)

    def test_operators(self):
        ua1 = UnlimitedAngle.from_degrees(degrees=1000)
        ua2 = UnlimitedAngle.from_degrees(degrees=2000)
        self.assertEqual(3000, (ua1 + ua2).to_degrees())
        self.assertEqual(1000, (ua2 - ua1).to_degrees())
        self.assertEqual(-1000, (ua1 - ua2).to_degrees())
        self.assertEqual(10000, (ua1 * 10).to_degrees())
        self.assertEqual(-1900, (ua1 / 10 - ua2).to_degrees())

    def test_trigonometric_functions(self):
        ua1 = UnlimitedAngle.from_dms(deg=30)
        self.assertAlmostEqual(0.50, ua1.sin(), delta=0.01)
        self.assertAlmostEqual(0.87, ua1.cos(), delta=0.01)
        self.assertAlmostEqual(0.57, ua1.tan(), delta=0.01)


if __name__ == "__main__":
    unittest.main()
