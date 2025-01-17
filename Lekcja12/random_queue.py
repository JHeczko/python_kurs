import random


class RandomQueue:
    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return self.__str__()

    def insert(self, item):
        if self.is_full():
            raise ValueError("Queue is full")
        self.items[self.n] = item
        self.n += 1

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        self.n -= 1
        choice = random.randint(0, self.n)
        data_rand = self.items[choice]
        data_end = self.items[self.n]
        if choice != self.n:
            self.items[choice] = data_end
        self.items[self.n] = None  # usuwam ostatni element
        return data_rand

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.n == self.size

    def clear(self):
        self.n = 0

if __name__ == '__main__':
    queue = RandomQueue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)
    queue.insert(5)
    print(queue)
    while not queue.is_empty():
        print("="*20)
        print(queue)
        print(queue.remove())
        print("=" * 20)