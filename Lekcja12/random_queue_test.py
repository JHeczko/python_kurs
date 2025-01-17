import pytest
from random_queue import RandomQueue

from random_queue import RandomQueue

class RandomQueueTest:
    @pytest.fixture(scope="class")
    def queue1(self):
        return RandomQueue()

    def test_empty(self, queue1):
        assert queue1.is_empty() is True
        queue1.insert(1)
        assert queue1.is_empty() is False
        queue1.remove()

    def test_


if __name__ == "__main__":
    pytest.main()