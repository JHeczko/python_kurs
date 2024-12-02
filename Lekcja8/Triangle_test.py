import pytest
from anyio.pytest_plugin import pytest_fixture_setup

from Triangle import Triangle
from Point import Point2D as Point

class TestTriangle:
    @pytest.fixture(scope="class")
    def tr1(self):
        return Triangle(0,0,0,6,6,0)

    @pytest.fixture(scope="class")
    def tr2(self):
        return Triangle(0,0,0,6,6,0)

    @pytest.fixture(scope="class")
    def tr3(self):
        return Triangle(2,2,2,4,4,4)

    @pytest.fixture(scope="class")
    def tr4(self):
        return Triangle(0,0,4,0,2,2)

    @pytest.mark.parametrize('points', [
        ([1,1,1,1,2,2]),
        ([1, 1, 1, 1, 1, 1]),
        ([2, 2, 1, 1, 1, 1]),
        ([2, 2, 1, 1, 3, 3])
    ])
    def test_init(self,points):
        with pytest.raises(ValueError):
            Triangle(*points)


    def test_rep(self, tr1, tr3):
        assert repr(tr1) == "Triangle(0.0, 0.0, 0.0, 6.0, 6.0, 0.0)"
        assert repr(tr3) == "Triangle(2.0, 2.0, 2.0, 4.0, 4.0, 4.0)"

    def test_str(self,tr1):
        assert str(tr1) == "[(0.0, 0.0), (0.0, 6.0), (6.0, 0.0)]"

    def test_eq(self, tr1,tr2,tr3):
        assert tr1 == Triangle(0,0,0,6,6,0)
        assert tr2 == Triangle(0,0,0,6,6,0)
        assert tr3 == Triangle(2,2,2,4,4,4)

    def test_ne(self,tr1):
        assert tr1 != Triangle(1,3,3,4,5,6)
    def test_center(self,tr1):
        assert tr1.center == Point(2, 2)

    def test_area(self, tr1,tr2,tr4):
        assert tr1.area() == tr2.area()
        assert tr4.area() == 4

    def test_move(self, tr1,tr2,tr3):
        assert tr1.move(2,2) == tr2.move(2,2)
        assert tr3.move(2,2) == Triangle(4,4,4,6,6,6)

    def test_make4(self, tr4):
        # celowo to tak przekombinowałem, ale chciałem zobaczyć działanie tych klauzuli with w testowaniu
        test_make4 = [Triangle(1, 1, 2, 0, 3, 1), Triangle(0, 0, 1, 1, 2, 0), Triangle(2, 0, 4, 0, 3, 1),
         Triangle(1, 1, 2, 2, 3, 1)]
        with pytest.raises(ValueError) as context:
            for triangle in tr4.make4():
                for tri_test in test_make4:
                    if tri_test == triangle:
                        flag = True
                if not flag:
                    raise ValueError("False")
            raise ValueError("True")
        assert str(context.value) == "True"

    def test_height(self, tr1):
        assert tr1.height == 6

    def test_rectangle(self, tr4):
        assert tr4.bottomleft == Point(0,0)
        assert tr4.bottomright == Point(4, 0)
        assert tr4.topleft == Point(0, 2)
        assert tr4.topright == Point(4, 2)

    @pytest.mark.parametrize('tr_comp, pt1, pt2, pt3', [
        (Triangle(0,0,4,0,2,2), Point(0,0), Point(4,0), Point(2,2)),
        (Triangle(2,2,2,4,4,4), Point(2, 2), Point(2, 4), Point(4, 4)),
        (Triangle(0,0,0,6,6,0), Point(0, 0), Point(0, 6), Point(6, 0))
    ])
    def test_fromPoints(self,tr_comp, pt1, pt2, pt3):
        assert Triangle.from_points([pt1,pt2,pt3]) == tr_comp
        assert Triangle.from_points((pt1,pt2,pt3)) == tr_comp

if __name__ == '__main__':
    pytest.main()