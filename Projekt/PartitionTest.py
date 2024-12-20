import pytest

from Projekt.Partition import Partition


class TestPartition:

    @pytest.fixture(scope='function')
    def partition1(self):
        return Partition(10)

    def test_partition1(self, partition1):
        assert partition1.size == 10

    def test_join(self,partition1):
        assert len(partition1.join({1},{4})) == 9
