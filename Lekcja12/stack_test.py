import pytest

from stack import Stack

class TestStack:
    @pytest.fixture(scope="class")
    def stack1(self):
        return Stack()

    def test_empty(self, stack1):
        assert stack1.is_empty() is True
        stack1.push(1)
        assert stack1.is_empty() is False
        stack1.pop()

    def test_push(self, stack1):
        with pytest.raises(ValueError) as context:
            while True:
                stack1.push(1)

    def test_full(self,stack1):
        assert stack1.is_full() is True

    def test_pop(self, stack1):
        assert stack1.pop() == 1
        with pytest.raises(ValueError) as context:
            while True:
                stack1.pop()

if __name__ == "__main__":
    pytest.main()
