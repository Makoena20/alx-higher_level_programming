#!/usr/bin/python3
"""Module for testing the Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_base_auto_id(self):
        """Test if Base assigns automatically an ID."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_base_auto_id_plus_one(self):
        """Test if Base assigns automatically an ID + 1 of the previous."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_base_custom_id(self):
        """Test if Base saves the ID passed."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_exists(self):
        """Test if Base.to_json_string(None) exists."""
        self.assertTrue(hasattr(Base, "to_json_string"))

    def test_to_json_string_empty_list_exists(self):
        """Test if Base.to_json_string([]) exists."""
        self.assertTrue(hasattr(Base, "to_json_string"))

    def test_to_json_string_list_with_dict_exists(self):
        """Test if Base.to_json_string([{'id': 12}]) exists."""
        self.assertTrue(hasattr(Base, "to_json_string"))

    def test_to_json_string_returns_string(self):
        """Test if Base.to_json_string([{'id': 12}]) returns a string."""
        self.assertIsInstance(Base.to_json_string([{'id': 12}]), str)

    def test_from_json_string_exists(self):
        """Test if Base.from_json_string(None) exists."""
        self.assertTrue(hasattr(Base, "from_json_string"))

    def test_from_json_string_empty_list_exists(self):
        """Test if Base.from_json_string("[]") exists."""
        self.assertTrue(hasattr(Base, "from_json_string"))

    def test_from_json_string_list_with_dict_exists(self):
        """Test if Base.from_json_string('[{"id": 89}]') exists."""
        self.assertTrue(hasattr(Base, "from_json_string"))

    def test_from_json_string_returns_list(self):
        """Test if Base.from_json_string('[{"id": 89}]') returns a list."""
        self.assertIsInstance(Base.from_json_string('[{"id": 89}]'), list)


if __name__ == '__main__':
    unittest.main()
