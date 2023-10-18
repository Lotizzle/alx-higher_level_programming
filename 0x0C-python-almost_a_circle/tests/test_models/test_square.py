#!/usr/bin/python3
"""This file defines unittests for models/square.py."""

import io
import unittest
from models.base import Base
from models.square import Square


class TestSquare_initialization(unittest.TestCase):
    """Unittests for testing initialization of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(12), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(1)
        s2 = Square(12)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(1, 2)
        s2 = Square(3, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(1, 2, 2)
        s2 = Square(3, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(8, Square(10, 2, 2, 8).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 3, 3, 10).size)

    def test_size_setter(self):
        s = Square(5, 3, 3, 10)
        s.size = 7
        self.assertEqual(7, s.size)

    def test_width_getter(self):
        s = Square(5, 3, 3, 10)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(5, 3, 3, 10)
        s.size = 9
        self.assertEqual(9, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquare_size_attribute(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.3)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

if __name__ == "__main__":
    unittest.main()
