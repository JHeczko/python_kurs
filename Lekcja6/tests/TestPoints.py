import unittest

from Lekcja6 import Point

class TestPoints(unittest.TestCase):
    def setUp(self):
        self.pt1 = Point(1, 2)
        self.pt11 = Point(1, 2)
        self.pt2 = Point(2, 4)
        self.pt3 = Point(0, 0)
        self.pt4 = Point(-3, -4)
        self.pt5 = Point(3, 4)

    def test_add(self):
        self.assertEqual(self.pt1 + self.pt11, self.pt2)
        self.assertEqual(self.pt4 + self.pt5, self.pt3)

    def test_sub(self):
        self.assertEqual(self.pt1 - self.pt1, self.pt3)
        self.assertEqual(self.pt4 - self.pt5, Point(-6,-8))

    def test_equal(self):
        self.assertEqual(self.pt1, self.pt11)

if __name__ == '__main__':
    unittest.main()