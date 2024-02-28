#!/usr/bin/python3
"""Module for unit tests for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_exists(self):
        """Test if Square class exists."""
        self.assertTrue(hasattr(Square, '__init__'))

    def test_square_inherits_base(self):
        """Test if Square inherits from Base."""
        self.assertTrue(issubclass(Square, Base))

    def test_square_attributes(self):
        """Test if Square instances have the proper attributes."""
        s = Square(5)
        self.assertTrue(hasattr(s, 'id'))
        self.assertTrue(hasattr(s, 'size'))
        self.assertTrue(hasattr(s, 'x'))
        self.assertTrue(hasattr(s, 'y'))

    def test_square_size(self):
        """Test if Square initializes with the correct size."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_size_error(self):
        """Test if Square raises errors for invalid size."""
        with self.assertRaises(ValueError):
            s = Square(-5)
        with self.assertRaises(TypeError):
            s = Square("five")

    def test_square_area(self):
        """Test if area() method returns the correct area."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_str(self):
        """Test if __str__() method returns the correct string."""
        s = Square(5)
        self.assertEqual(str(s), '[Square] (1) 0/0 - 5')

    def test_square_update(self):
        """Test if update() method correctly updates attributes."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (1) 3/4 - 2')

    def test_square_update_kwargs(self):
        """Test if update() method correctly updates with kwargs."""
        s = Square(5)
        s.update(id=2, size=3, x=4, y=5)
        self.assertEqual(str(s), '[Square] (2) 4/5 - 3')

    def test_square_to_dictionary(self):
        """Test if to_dictionary() method returns the correct dictionary."""
        s = Square(5, 6, 7, 8)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {'id': 8, 'size': 5, 'x': 6, 'y': 7})


if __name__ == '__main__':
    unittest.main()
