#!/usr/bin/python3

"""
Unit t
estifor max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test the max_integer function
    """
    def test_max_integer(self):
        result = max_integer([1, 4, 3, 2])
        self.assertEqual(result, 4)
        result = max_integer([12, 9, 7, 2])
        self.assertEqual(result, 12)

    def test_isint(self):
        var = 1
        self.assertTrue(max_integer([var, 2]) == 2)
        x = 5
        self.assertTrue(max_integer([1, x]) == x)

    def test_one_entry(self):
        self.assertEqual(max_integer([10]), 10)

    def test_negative_integer(self):
        self.assertEqual(max_integer([-1, -2, -5]), -1)

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)

    def test_same_entry(self):
        a = 50
        self.assertEqual(max_integer([a, a, a, a]), a)

    def test_float_integer(self):
        self.assertEqual(max_integer([4.0, 3, 2]), 4.0)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

        if __name__ == '__main__':
            unittest.main()
