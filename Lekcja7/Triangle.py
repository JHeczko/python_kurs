import itertools
import unittest
from decimal import DivisionByZero

from matplotlib import pyplot as plt

from Point import Point2D as Point

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        self.pts = [self.pt1, self.pt2, self.pt3]
        a = []
        for p1,p2 in itertools.combinations(self.pts, 2):
            if (p1.x - p2.x) == 0:
                a.append(0)
            else:
                a.append((p1.y - p2.y) / (p1.x - p2.x))
        if a[0] == a[1] and a[0] == a[2] and a[1] == a[2]:
            raise ValueError("It is not a Triangle, but a line")
        if self.pt1 == self.pt2 or self.pt3 == self.pt1 or self.pt2 == self.pt3:
            raise ValueError("At least two points are the same")


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

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

        # zwraca środek (masy) trójkąta
    def center(self):
        return Point(sum(i.x for i in self) / 3, sum(i.y for i in self) / 3)


    def __iter__(self):
        return iter([self.pt1, self.pt2, self.pt3])

    # pole powierzchni
    def area(self):
        return 0.5 * abs(
            self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y))

        # przesunięcie o (x, y

    def move(self, x, y):
        for pt in self:
            pt.x += x
            pt.y += y
        return self

    def make4(self):
        buf = {self.pt1: [], self.pt2: [], self.pt3: []}
        third = []
        for p1,p2 in itertools.combinations(self.pts, 2):
            pt = Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)
            buf[p1].append(pt)
            buf[p2].append(pt)
            third.append(pt.x)
            third.append(pt.y)
        tri = []
        for key,val in buf.items():
            tri.append(Triangle(key.x, key.y, val[0].x, val[0].y, val[1].x, val[1].y))
        tri.append(Triangle(*third))
        return tuple(tri)

    def show_triangle(self, *args):
        for pt in self:
            plt.scatter(pt.x,pt.y, marker='o', color='red')
        for tri in args:
            for pt in tri:
                plt.scatter(pt.x,pt.y, marker='o')
        plt.show()

#     A       po podziale    A
#    / \                    / \
#   /   \                  +---+
#  /     \                / \ / \
# C-------B              C---+---B

class TestTriangle(unittest.TestCase):
    def setUp(self): pass


if __name__ == '__main__':
    unittest.main()