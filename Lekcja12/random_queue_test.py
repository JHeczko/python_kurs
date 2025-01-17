import pytest
from random_queue import RandomQueue

from random_queue import RandomQueue

class TestRandomQueue:
    @pytest.fixture(scope="class")
    def queue1(self):
        return RandomQueue(size=5)

    def test_empty(self, queue1):
        assert queue1.is_empty() is True
        queue1.insert(1)
        assert queue1.is_empty() is False
        queue1.remove()

    def test_insert_remove(self,queue1):
        arr = [1,2,3,4,5]
        for x in arr:
            queue1.insert(x)
        arr_check = []
        while not queue1.is_empty():
            arr_check.append(queue1.remove())
        assert set(arr_check) == set(arr)
        for x in arr:
            queue1.insert(x)


    def test_full(self, queue1):
        assert queue1.is_full() is True
        queue1.remove()
        assert queue1.is_full() is False
        queue1.insert(1)
        assert queue1.is_full() is True

    def test_clear(self, queue1):
        queue1.clear()
        assert queue1.is_empty() is True


if __name__ == "__main__":
    pytest.main()