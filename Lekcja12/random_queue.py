# ZADANIE 12.8 (RANDOMQUEUE)
#
# Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności. Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.
class RandomQueue:
    def __init__(self, size=10): pass

    def insert(self, item): pass   # wstawia element w czasie O(1)

    def remove(self): pass   # zwraca losowy element w czasie O(1)

    def is_empty(self): pass

    def is_full(self): pass

    def clear(self): pass   # czyszczenie listy