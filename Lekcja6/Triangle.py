from .Shape import Shape
from .Point import Point2D as Point

class Triangle(Shape):

    """Klasa reprezentująca trójkąt na płaszczyźnie."""
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __iter__(self):
        return iter([self.pt1, self.pt2, self.pt3])

    # "[(x1, y1), (x2, y2), (x3, y3)]"
    def __str__(self):
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

    # "Triangle(x1, y1, x2, y2, x3, y3)"
    def __repr__(self):
        return f"Triangle({self.pt1['x']}, {self.pt1['y']}, {self.pt2['x']}, {self.pt2['y']}, {self.pt3['x']}, {self.pt3['y']})"

    # obsługa tr1 == tr2
    # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
    # niezależnie od kolejności pt1, pt2, pt3.
    def __eq__(self, other):
        flag = True
        for pt in self:
            for pt2 in other:
                if pt == pt2:
                    flag = False
            if flag:
                return False
        return True


    # obsługa tr1 != tr2
    def __ne__(self, other):
        return not self.__eq__(other)

    # zwraca środek (masy) trójkąta
    def center(self):
        return Point(sum(i.x for i in self)/3, sum(i.y for i in self)/3)

    # pole powierzchni
    def area(self):
        return 0.5 * abs(self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y))

    # przesunięcie o (x, y
    def move(self, x, y):
        for pt in self:
            pt.x += x
            pt.y += y
        return self
