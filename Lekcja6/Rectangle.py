from .Point import Point2D as Point
from .Shape import Shape

"""Klasa reprezentująca prostokąt na płaszczyźnie."""
class Rectangle(Shape):

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        if self.pt1 == self.pt2:
            raise ValueError("This is a point not a rectangle")

    # "[(x1, y1), (x2, y2)]"
    def __str__(self): pass

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self): pass

    # obsługa rect1 == rect2
    def __eq__(self, other): pass

    # obsługa rect1 != rect2
    def __ne__(self, other):
        return not self == other

    # zwraca środek prostokąta
    def center(self): pass

    # pole powierzchni
    def area(self): pass

    # przesunięcie o (x, y)
    def move(self, x, y): pass
