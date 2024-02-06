#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([..])"""

    def test_max_positive_integers(self):
        """Test the max_integer function with a list of positive integers."""
        self.assertEqual(max_integer([5, 4, 3, 1]), 5)

    def test_max_negative_integers(self):
        """Test the max_integer function with a list of negative integers."""
        self.assertEqual(max_integer([-2, -8, -5, -1]), -1)

    def test_max_mixed_integers(self):
        """Test the max_integer function with a list of mixed
        positive and negative integers."""
        self.assertEqual(max_integer([10, -3, 7, -8]), 10)

    def test_with_floats(self):
        """Test the max_integer function with a list of
        floating-point numbers."""
        self.assertEqual(max_integer([1.45, -3.89, 7.90, -8.98]), 7.90)

    def test_with_fractions(self):
        """Test the max_integer function with a list of fractional numbers."""
        self.assertEqual(max_integer([0.10, -0.3, 0.7, -0.8]), 0.7)

    def test_max_duplicate_integers(self):
        """Test the max_integer function with a list of duplicate integers."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_max_empty_list(self):
        """Test the max_integer function with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_max_single_element_list(self):
        """Test the max_integer function with a list containin
         a single element."""
        self.assertEqual(max_integer([42]), 42)

    def test_max_none_list(self):
        """Test the max_integer function with a None argument."""
        self.assertIsNone(max_integer(""), None)

    def test_max_strings(self):
        """Test the max_integer function with a list of strings."""
        self.assertEqual(max_integer(['apple', 'banana', 'grape', 'orange']),
                         'orange')

    def test_max_at_end(self):
        """Test a list with max value at the end."""
        test_list = [2, 3, 10, 5, 6, 100]
        self.assertEqual(max_integer(test_list), 100)

    def test_max_at_middle(self):
        """Test a list with max value in between."""
        test_list = [2, 3, 10, 5, 6]
        self.assertEqual(max_integer(test_list), 10)


if __name__ == '__main__':
    unittest.main()
