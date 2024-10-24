def prg(skk): return ("\033[92m {}\033[00m" .format(skk))
def prr(skk): return ("\033[91m {}\033[00m" .format(skk))

# ZADANIE 3.1
print(prg("# ZADANIE 3.1: Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?\n"))
print(prg("# Kod: x = 2; y = 3;\n# if (x > y):\n#     result = x;\n# else:\n#     result = y;"))
print(prr("W języku typu C, byłoby to niepoprawne, ale w Pythonie działa poprawnie. W Pythonie zmienne są dostępne w obrębie funkcji, klasy lub modułu. Instrukcje if/else nie tworzą nowego zasięgu zmiennych."))
print("="*40)

# for i in "axby": if ord(i) < 100: print (i)
print(prg("# ZADANIE 3.1: Kod 2"))
print(prg('for i in "axby": if ord(i) < 100: print (i)'))
print(prr("Ten kod nie zadziała, ponieważ if nie może być zagnieżdżony w jednej linii z for. Należy sformatować kod odpowiednio białymi znakami."))
print("="*40)

# for i in "axby": print (ord(i) if ord(i) < 100 else i)
print(prg("# ZADANIE 3.1: Kod 3"))
print(prg("for i in 'axby': print (ord(i) if ord(i) < 100 else i)"))
print(prr("Ten kod działa poprawnie, ponieważ używamy wyrażenia warunkowego w jednej linii."))
print("="*40)

# ZADANIE 3.2
print(prg("# ZADANIE 3.2: Co jest złego w poniższym kodzie?\n"))
print(prg("L = [3, 5, 4] ; L = L.sort()"))
print(prr("Problem: sort() działa in-place i nie zwraca posortowanej listy, więc L = L.sort() przypisuje None do L. Poprawka: użyj sorted(L)."))
print(prg("x, y = 1, 2, 3"))
print(prr("Problem: próbujemy przypisać 3 elementy do 2 zmiennych, co powoduje błąd."))
print(prg("X = [1, 2, 3] ; X[3] = 4"))
print(prr("Problem: indeks 3 wykracza poza zakres, ponieważ lista jest indeksowana od 0."))
print(prg('X = "abc" ; X.append("d")'))
print(prr("Problem: Stringi w Pythonie są niemutowalne i nie mają metody append()."))
print(prg("L = list(map(pow, range(8)))"))
print(prr("Problem: pow() potrzebuje dwóch argumentów, więc nie można jej bezpośrednio użyć w map()."))
print("="*40)

# ZADANIE 3.3
print(prg("# ZADANIE 3.3: Wypisać liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.\n"))
for i in range(0, 31):
    if i % 3 != 0:
        print(prr(i), end=' ', flush=True)
