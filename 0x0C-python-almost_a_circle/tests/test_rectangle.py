import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle_creation(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_area(self):
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
