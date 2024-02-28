#!/usr/bin/python3
"""
Unit Test for Rectangle Class
"""

import unittest
import json
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_init(self):
        """Test constructor"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_area(self):
        """Test area method"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        """Test __str__ method"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        """Test display method"""
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        self.assertEqual(r.display(), expected_output)

    def test_update(self):
        """Test update method"""
        r = Rectangle(1, 1)
        r.update(10, 2, 3, 4, 5)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            saved_json = file.read()
        expected_json = json.dumps([r1.to_dictionary(), r2.to_dictionary()])
        self.assertEqual(saved_json, expected_json)

    def test_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertTrue(isinstance(loaded_rectangles, list))
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertTrue(all(isinstance(r, Rectangle) for r in loaded_rectangles))
        self.assertEqual(loaded_rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded_rectangles[1].to_dictionary(), r2.to_dictionary())


if __name__ == '__main__':
    unittest.main()
