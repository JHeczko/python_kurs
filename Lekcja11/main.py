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
            yield node.data
            node = node.next

    def __del__(self):
        self.clear()

    # TODO te 3 metody
    def remove_tail(self): pass   # klasy O(n)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.

    def join(self, other): pass   # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.

    def clear(self):
        self.head = None

if __name__ == '__main__':
    # Single test
    slist = SingleList()
    slist.insert_head(Node(11))  # [11]
    slist.insert_head(Node(22))  # [22, 11]
    slist.insert_tail(Node(33))  # [22, 11, 33]
    for item in slist:  # kolejność 22, 11, 33
        print(item)