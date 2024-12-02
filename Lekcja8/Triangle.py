import itertools
import numpy as np

#*
# Wzbogacić klasę Triangle o nowe funkcjonalności (plik triangles.py).
#
# Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć trójkąt z listy lub krotki zawierającej trzy punkty. Wywołanie:
# triangle = Triangle.from_points((point1, point2, point3))
#
# Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę (współrzędną tylko do odczytu): top, left, bottom, right, width, height.
#
# Dodać atrybuty wirtualne zwracające Point (tylko do odczytu): topleft, bottomleft, topright, bottomright. Wymienione atrybuty wirtualne opisują prostokąt ograniczający dany trójkąt (bounding box).
#
# Można rozważyć zamianę metody center() na atrybut wirtualny.
#
# W osobnym pliku (test_triangles.py) przygotować testy klasy Triangle w formacie dla modułu 'pytest'.
# #

from matplotlib import pyplot as plt
from Point import Point2D as Point

class Triangle:

    @staticmethod
    def from_points(p_list):
        p1,p2,p3 = p_list
        return Triangle(p1.x,p1.y,p2.x,p2.y,p3.x,p3.y)

    def __init__(self, x1, y1, x2, y2, x3, y3):
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


    def __str__(self):
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"


    def __repr__(self):
        return f"Triangle({self.pt1['x']}, {self.pt1['y']}, {self.pt2['x']}, {self.pt2['y']}, {self.pt3['x']}, {self.pt3['y']})"

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

    def __iter__(self):
        return iter([self.pt1, self.pt2, self.pt3])

    def __hash__(self):
        return hash(tuple(sorted(self.pts)))

    @property
    def center(self):
        return Point(sum(i.x for i in self) / 3, sum(i.y for i in self) / 3)

    def area(self):
        return 0.5 * abs(
            self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y))


    def move(self, x, y):
        self.pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        self.pt2 = Point(self.pt2.x + x, self.pt2.y + y)
        self.pt3 = Point(self.pt3.x + x, self.pt3.y + y)
        return self

    def make4(self):
        #buf = {self.pt1: [], self.pt2: [], self.pt3: []}
        buf = {str(self.pt1): [self.pt1], str(self.pt2): [self.pt2], str(self.pt3): [self.pt3]}
        third = []
        for p1,p2 in itertools.combinations(self.pts, 2):
            pt = Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)
            buf[str(p1)].append(pt)
            buf[str(p2)].append(pt)
            third.append(pt.x)
            third.append(pt.y)
        tri = []
        for key,val in buf.items():
            tri.append(Triangle(val[0].x, val[0].y, val[1].x, val[1].y, val[2].x,val[2].y))
        tri.append(Triangle(*third))
        return tuple(tri)

    def show_triangle(self, *args):
        # for itself
        for pt in self:
            plt.scatter(pt.x,pt.y, marker='o', color='red')
        for pt1,pt2 in itertools.combinations(self.pts, 2):
            plt.plot([pt1.x, pt2.x], [pt1.y, pt2.y], color='blue')

        # for different triangles
        for tri in args:
            for pt in tri:
                plt.scatter(pt.x,pt.y, marker='o')
            for pt1, pt2 in itertools.combinations(tri.pts, 2):
                plt.plot([pt1.x, pt2.x], [pt1.y, pt2.y], color='blue')
        plt.show()

    @property
    def width(self):
        return np.sqrt((self.pt1.x - self.pt2.x) ** 2 + (self.pt1.y - self.pt2.y) ** 2)

    @property
    def height(self):
        return 2*self.area() / self.width

    @property
    def bottomleft(self):
        pts_x = [self.pt1.x, self.pt2.x, self.pt3.x]
        pts_y = [self.pt1.y, self.pt2.y, self.pt3.y]
        x_min = np.min(pts_x)
        y_min = np.min(pts_y)
        return Point(x_min, y_min)

    @property
    def topleft(self):
        pts_x = [self.pt1.x, self.pt2.x, self.pt3.x]
        pts_y = [self.pt1.y, self.pt2.y, self.pt3.y]
        x_min = np.min(pts_x)
        y_max = np.max(pts_y)
        return Point(x_min, y_max)

    @property
    def topright(self):
        pts_x = [self.pt1.x, self.pt2.x, self.pt3.x]
        pts_y = [self.pt1.y, self.pt2.y, self.pt3.y]
        x_max = np.max(pts_x)
        y_max = np.max(pts_y)
        return Point(x_max, y_max)

    @property
    def bottomright(self):
        pts_x = [self.pt1.x, self.pt2.x, self.pt3.x]
        pts_y = [self.pt1.y, self.pt2.y, self.pt3.y]
        x_max = np.max(pts_x)
        y_min = np.min(pts_y)
        return Point(x_max, y_min)