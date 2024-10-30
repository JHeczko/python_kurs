# Funkcje do kolorowania tekstu
def prRed(skk): return "\033[91m {}\033[00m".format(skk)
def prGreen(skk): return "\033[92m {}\033[00m".format(skk)
def prYellow(skk): return "\033[93m {}\033[00m".format(skk)
def prLightPurple(skk): return "\033[94m {}\033[00m".format(skk)
def prPurple(skk): return "\033[95m {}\033[00m".format(skk)
def prCyan(skk): return "\033[96m {}\033[00m".format(skk)
def prLightGray(skk): return "\033[97m {}\033[00m".format(skk)
def prBlack(skk): return "\033[98m {}\033[00m".format(skk)


# Zadanie 4.2
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.
# Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.
def make_ruler(x):
    ruler = "|...." * x + "|\n"
    for i in range(x + 1):
        ruler += f'{i:>5}'
    return ruler + "\n"

def make_grid(col, row):
    grid = ""
    for y in range(col):
        grid += ("+---" * row + "+\n" + "|   " * row + "|\n")
    grid += "+---" * row + "+"
    return grid + "\n"

print(prYellow("Zadanie 4.2:"))
print(prYellow("Wynik make_ruler(10):\n"), prCyan(make_ruler(10)))
print(prYellow("Wynik make_grid(10, 5):\n"), prCyan(make_grid(10, 5)))


# Zadanie 4.3
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x

print(prYellow("\nZadanie 4.3:"))
print(prYellow("Wynik factorial(5):"), prGreen(factorial(5)))


# Zadanie 4.4
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
def fibonacci(n):
    if n in [1, 2]:
        return 1
    prev, curr = 1, 1
    for _ in range(2, n):
        prev, curr = curr, prev + curr
    return curr

print(prYellow("\nZadanie 4.4:"))
print(prYellow("Wynik fibonacci(6):"), prGreen(fibonacci(6)))


# Zadanie 4.5
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
def odwracanie_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def odwracanie_rek(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left + 1, right - 1)

L_iter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
L_rek = L_iter[:]
odwracanie_iter(L_iter, 4, 8)
odwracanie_rek(L_rek, 4, 8)

print(prYellow("\nZadanie 4.5:"))
print(prYellow("Wynik odwracanie_iter i odwracanie_rek:"))
print(prGreen(f"L_iter: {L_iter}"))
print(prGreen(f"L_rek: {L_rek}"))


# Zadanie 4.6
# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(prYellow("\nZadanie 4.6:"))
print(prYellow("Wynik sum_seq(seq):"), prGreen(sum_seq(seq)))


# Zadanie 4.7
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
def flatten(sequence):
    flat_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

print(prYellow("\nZadanie 4.7:"))
print(prYellow("Wynik flatten(seq):"), prGreen(flatten(seq)))
