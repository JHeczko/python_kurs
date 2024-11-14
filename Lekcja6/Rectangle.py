from .Point import Point2D as Point
from .Shape import Shape
import numpy as np

"""Klasa reprezentująca prostokąt na płaszczyźnie."""
class Rectangle(Shape):

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        if self.pt1 == self.pt2:
            raise ValueError("This is a point not a rectangle")

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):
        return f"Rectangle({self.pt1['x']}, {self.pt1['y']}, {self.pt2['x']}, {self.pt2['y']})"

    # obsługa rect1 == rect2
    def __eq__(self, other):
        if self.pt1 != other.pt1 and self.pt1 != other.pt2:
            return False
        if self.pt2 != other.pt1 and self.pt2 != other.pt2:
            return False
        return True

    # obsługa rect1 != rect2
    def __ne__(self, other):
        return not self == other

    # zwraca środek prostokąta
    def center(self):
        return Point((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)

    # pole powierzchni
    def area(self):
        return np.abs(self.pt1.x - self.pt2.x) * np.abs(self.pt1.x - self.pt2.x)

    # przesunięcie o (x, y)
    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self
