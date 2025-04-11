
# test_calculator.py

import unittest
from calculator import add, subtract, multiply, is_even

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

if __name__ == '__main__':
    unittest.main()
