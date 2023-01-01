#!/usr/bin/python3

"""
Unit t
estifor max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerMethod(unittest.TestCase):

    """Method test for max_integer function"""

    def test_data_types(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer((2, 4, 12)), 12)
        self.assertEqual(max_integer(['a', 'A', 'c', 'C']), 'c')
        self.assertEqual(max_integer([43, 100, 535, 22, 655, 7, 112]), 655)

    def test_same_number(self):
        self.assertTrue(max_integer([7, 7, 7, 7]) == 7)

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            max_integer(7)
