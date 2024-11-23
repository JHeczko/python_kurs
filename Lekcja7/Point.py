import numpy as np

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __idiv__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise KeyError
        if key == 'x':
            return self.x
        elif key == 'y':
            return self.y

    def __len__(self):
        return np.sqrt(self.x ** 2 + self.y ** 2)
