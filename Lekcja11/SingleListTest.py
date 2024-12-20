import pytest
from SingleList import SingleList,Node

class TestSingleList:
    @pytest.fixture(scope='function')
    def list1(self):
        slist = SingleList()
        slist.insert_head(Node(11))  # [11]
        slist.insert_head(Node(22))  # [22, 11]
        slist.insert_tail(Node(33))  # [22, 11, 33]
        return slist
    @pytest.fixture(scope='function')
    def list2(self):
        slist2 = SingleList()
        slist2.insert_head(Node(3))  # [3]
        slist2.insert_head(Node(2))  # [2, 3]
        slist2.insert_tail(Node(1))  # [2, 3, 1]
        return slist2

    def test_equal(self,list1,list2):
        assert list1 != list2
        assert list1 == list1
        assert list1 != [1,3,5,2,124]
        assert list1 == [22,11,33]

    def test_insert(self,list1):
        list1.insert_head(Node(11))
        assert list1 == list1
        assert list1 == [11,22,11,33]

        list1.insert_tail(Node(33))
        assert list1 == [11, 22, 11, 33, 33]

        node = list1.remove_head()
        assert list1 == [22, 11, 33, 33]
        assert node == Node(11)

        node = list1.remove_tail()
        assert list1 == [22, 11, 33]
        assert node == Node(33)

    def test_str(self,list1,list2):
        assert str(list1) == '[22, 11, 33]'
        assert str(list2) == '[2, 3, 1]'

    def test_len(self,list1,list2):
        assert len(list1) == len(list2)
        list2.insert_tail(Node(11))
        assert len(list1) != len(list2)

    def test_clear_empty(self,list1):
        list1.clear()
        assert list1.is_empty() == True

    def test_join(self,list1,list2):
        list1.join(list2)
        assert list1 != list2
        assert list1.is_empty() == False
        assert list2.is_empty() == True
        assert list1 == [22,11,33,2,3,1]

if __name__ == '__main__':
    pytest.main()