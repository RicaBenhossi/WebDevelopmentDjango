import unittest

from circle import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def teste_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), (pi * (2.1**2)))
