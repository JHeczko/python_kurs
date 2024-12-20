import itertools
from os import terminal_size


class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
            return not self == other


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def __iter__(self):   # wykorzystanie funkcji generatora
        node = self.head
        while node:
            yield node
            node = node.next

    def __del__(self):
        for node in self:
            next_node = node.next
            if next_node is None:
                node.next = None
                del node
                break
            else:
                node.next = None
                del node



        self.clear()

    def __len__(self):
        return self.length

    def __str__(self):
        return str(f"{[int(str(x)) for x in self]}")

    # Funckja uzywana wylacznie do testow ze wzgledu na lepsza czytelności co do czego porównujemy czytelnosc
    def _to_array(self):
        return [x.data for x in self]

    def __eq__(self, other):
        x_i = self.__iter__()
        y_i = other.__iter__()

        for x,y in itertools.zip_longest(x_i, y_i):
            if (x is None) ^ (y is None):
                return False
            if type(other) == list:
                if x.data != y:
                    return False
            if type(other) == SingleList:
                if x != y:
                    return False
        return True

    def remove_tail(self): # klasy O(n)
        if self.is_empty():
            raise ValueError("Empty list")

        x_prev = self.head
        for x in self:
            if x.next is None:
                self.tail = x_prev
                self.tail.next = None
                self.length -= 1
                x.next = None
                return x
            else:
                x_prev = x

    def join(self, other): # klasy O(1)
        self.tail.next = other.head
        self.tail = other.tail
        self.length += other.length
        other.clear()

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

#
if __name__ == '__main__':
    # Single test
    slist = SingleList()
    slist2 = SingleList()
    slist.insert_head(Node(11))  # [11]
    slist.insert_head(Node(22))  # [22, 11]
    slist.insert_tail(Node(33))  # [22, 11, 33]

    slist2.insert_head(Node(3))  # [11]
    slist2.insert_head(Node(2))  # [22, 11]
    slist2.insert_tail(Node(1))  # [22, 11, 33]

    print(slist, slist2, len(slist),len(slist2))

    slist.join(slist2)

    print(slist,slist2,len(slist),len(slist2))
