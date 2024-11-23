#*
# ZADANIE 7.6 (ITERATORY)
# Stworzyć następujące iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...,
# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
# *#
import itertools
import random
from tabnanny import check


def check_it(it):
    print('\n' + "-" * 15+"Iter test"+ "-" * 15 + '\n', end='')
    for i,x in enumerate(it):
        if i == 20:
            break
        else:
            print(x, end=' ')
    print('\n'+"-"*39+'\n')

if __name__ == '__main__':
# a
    it = itertools.cycle(range(0,2))
    check_it(it)
# b
    it = iter(lambda: ("W","E","N","S")[random.randint(0,3)],-1)
    check_it(it)
# c
    it = (random.randint(0,6) for _ in iter(int,-1))
    check_it(it)