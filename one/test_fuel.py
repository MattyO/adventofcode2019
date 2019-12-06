import unittest
import fuel

class CalculateTest(unittest.TestCase):

    def test_calculate_twelve(self):
        self.assertEqual(fuel.calculate(12), 2)

    def test_calculate_14(self):
        self.assertEqual(fuel.calculate(14), 2)

    def test_calculate_1969(self):
        self.assertEqual(fuel.calculate(1969), 654)

    def test_calculate(self):
        self.assertEqual(fuel.calculate(100756), 33583)

    def test_total_calc(self):
        self.assertEqual(fuel.total_calc('data.txt'), 3311492)

    def test_rcalc_14(self):
        self.assertEqual(fuel.rcalc(14), 2)

    def test_rcalc_1969(self):
        self.assertEqual(fuel.rcalc(1969), 966)

    def test_rcalc_100756(self):
        self.assertEqual(fuel.rcalc(100756), 50346)

    def test_total_rcalc(self):
        self.assertEqual(fuel.total_rcalc('data.txt'), 3311492)


