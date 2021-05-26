#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_one(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    def test_value(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -3, 4, 2]), 4)
    def test_float(self):
        self.assertEqual(max_integer([0.00, 2, -3, 1]), 2)
        self.assertEqual(max_integer([-1, -3, 0.0, 2]), 2)
    def test_empy(self):
        self.assertEqual(max_integer([]), None)
    def test_m(self):
        self.assertEqual(max_integer([2, 4, 1]), 4)
    def test_t(self):
        self.assertIs(list, list)
    def test_equal(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
    def test_same(self):
        self.assertEqual(max_integer([2, 3, 1, 3]), 3)
        self.assertEqual(max_integer([1, 0.0, 0.5, 1]), 1)
    def test_same(self):
        self.assertEqual(max_integer([2, 3, 1, 3]), 3)
        self.assertEqual(max_integer([1, 0.0, 0.5, 1]), 1)
    def test_same(self):
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([1]), 1)
    def test_same(self):
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([1]), 1)
    def test_string(self):
        self.assertEqual(max_integer(['d', 'e', 'm']), 'm')
    def test_diferent(self):
        with self.assertRaises(TypeError):
            max_integer(['r', 5, 2])
    def test_n(self):
        with self.assertRaises(TypeError):
            max_integer([None, 4])

if __name__ == '__main__':
    unittest.main()
