import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create_instance(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def test_create_instance_with_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_create_multiple_instances(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)


if __name__ == '__main__':
    unittest.main()
