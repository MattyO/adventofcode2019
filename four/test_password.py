import unittest
from password import is_valid, is_valid2


class PasswordTest(unittest.TestCase):

    def test_valid_length(self):
        self.assertTrue(is_valid(111111))

    def test_valid_has_double(self):
        self.assertTrue(is_valid(123455))

    def test_always_increases(self):
        self.assertFalse(is_valid(223450))

    def test_has_double(self):
        self.assertFalse(is_valid(123789))

    def test_no_double_pair(self):
        self.assertTrue(is_valid2(112233))

    def test_no_double_pair2(self):
        self.assertFalse(is_valid2(123444))

    def test_no_double_pair3(self):
        self.assertTrue(is_valid2(111122))

    def test_is_valid_answer(self):
        self.assertEqual(sum([ is_valid(n) for n in range(347312, 805915) ]), 594)

    def test_is_valid2_answer(self):
        self.assertEqual(sum([ is_valid2(n) for n in range(347312, 805915) ]), 364)
