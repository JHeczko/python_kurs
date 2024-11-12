# import unittest
# from Lekcja6 import Rectangle
#
#
# class TestRectangle(unittest.TestCase):
#     def setUp(self):
#         self.tr1 = Rectangle(1,2,3,4)
#         self.tr2 = Rectangle(1,2,3,4)
#         self.tr3 = Rectangle(2,2,4,4)
#
#     def test_rep(self):
#         self.assertEqual(repr(self.tr1), "Rectangle(1, 2, 3, 4)")
#
#     def test_str(self):
#         self.assertEqual(str(self.tr1), "[(1, 2), (3, 4)]")
#
#     def test_eq(self):
#         self.assertEqual(self.tr1, Rectangle(1,2,3,4))
#         self.assertEqual(self.tr2, Rectangle(1,2,3,4))
#         self.assertEqual(self.tr3, Rectangle(2,2,4,4))
#
#     def test_ne(self):
#         self.assertNotEqual(self.tr1, Rectangle(1,3,3,4))
#
#     def test_center(self): pass
#
#     def test_area(self):
#         self.assertEqual(self.tr1.area(), self.tr2.area())
#         self.assertEqual(self.tr3.area(), 4)
#
#     def test_move(self):
#         self.assertEqual(self.tr1.move(2,2), self.tr2.move(2,2))
#         self.assertEqual(self.tr3.move(2,2), Rectangle(4,4,6,6))