import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_creation(self):
        s = Square(5, 6, 7)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)

    def test_square_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
