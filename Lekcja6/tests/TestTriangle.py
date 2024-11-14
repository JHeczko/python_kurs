import unittest

from Lekcja6 import Triangle,Point

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.tr1 = Triangle(1,2,3,4,5,6)
        self.tr2 = Triangle(1,2,3,4,5,6)
        self.tr3 = Triangle(2,2,2,4,4,4)
        self.tr4 = Triangle(0,0,4,0,2,2)

    def test_init(self):
        self.assertRaises(TypeError, Triangle.__init__, 1,1,1,1,2,2)
        self.assertRaises(TypeError, Triangle.__init__, 1, 1, 1, 1, 1, 1)
        self.assertRaises(TypeError, Triangle.__init__, 2, 2, 1, 1, 1, 1)
    def test_rep(self):
        self.assertEqual(repr(self.tr1), "Triangle(1, 2, 3, 4, 5, 6)")
        self.assertEqual(repr(self.tr3), "Triangle(2, 2, 2, 4, 4, 4)")

    def test_str(self):
        self.assertEqual(str(self.tr1), "[(1, 2), (3, 4), (5, 6)]")

    def test_eq(self):
        self.assertEqual(self.tr1, Triangle(1,2,3,4,5,6))
        self.assertEqual(self.tr2, Triangle(1,2,3,4,5,6))
        self.assertEqual(self.tr3, Triangle(2,2,2,4,4,4))

    def test_ne(self):
        self.assertTrue(self.tr1!=Triangle(1,3,3,4,5,6))

    def test_center(self):
        print()
        self.assertEqual(self.tr1.center(), Point(3, 4))

    def test_area(self):
        self.assertEqual(self.tr1.area(), self.tr2.area())
        self.assertEqual(self.tr4.area(), 4)

    def test_move(self):
        self.assertEqual(self.tr1.move(2,2), self.tr2.move(2,2))
        self.assertEqual(self.tr3.move(2,2), Triangle(4,4,4,6,6,6))

if __name__ == '__main__':
    unittest.main()