def prg(skk): return ("\033[92m> {}\033[00m" .format(skk))
def prr(skk): return ("\033[91m{}\033[00m" .format(skk))

# ZADANIE 3.5
print(prg("ZADANIE 3.5: Napisać program rysujący miarkę o zadanej długości."))
x = 30
print('|....'*x, end='', flush=True)
print('|')
for i in range(0,x+1):
    if i == 0:
        print(i, end='')
    else:
        print(f'{i:>5}',end='')
print('\n')

# ZADANIE 3.6
print(prg("ZADANIE 3.6: Napisać program rysujący prostokąt zbudowany z małych kratek."))
width = 4
height = 3
for y in range(0,height):
    print("+---"*width,end='', flush=True)
    print('+')
    print("|   "*width,end='', flush=True)
    print('|')
    if(y==height-1):
        print("+---"*width,end='', flush=True)
        print('+')
print('\n')

# ZADANIE 3.8
print(prg("ZADANIE 3.8: Znaleźć wspólne i unikalne elementy z dwóch sekwencji liczb lub znaków."))
L1 = (1,23,4,34,1,31,3,123,12,312,3,12,4,5,9,87,97,65,465)
L2 = (23,124,43,1,3,9,312,312,31,25534,8,598,45,5243)
common = list(set(L1).intersection(set(L2)))
print(prr("Wspólne elementy:"))
print(common)
print('\n')

# ZADANIE 3.9
print(prg("ZADANIE 3.9: Znaleźć listę sum dla poszczególnych sekwencji liczb."))
L3 = [[],[4],(1,2),[3,4],(5,6,7),(1,23,4,34,1,31,3,123,12,312,3,12,4,5,9,87,97,65,465)]
sum_all = [sum(list) for list in L3]
print(prr("Suma elementów w sekwencjach:"))
print(sum_all)
print('\n')

# ZADANIE 3.10
print(prg("ZADANIE 3.10: Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim na liczby arabskie."))
roman_word = 'CDXLIV' # 444
def roman2int(x):
    V = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    previous = 0
    for c in reversed(x):
        if V[c] >= previous:
            total += V[c]
            previous = V[c]
        else:
            total -= V[c]
            previous = V[c]
    return total
print(prr("Wartość liczby rzymskiej 'CDXLIV':"))
print(roman2int(roman_word))

# Różne sposoby tworzenia słowników
print(prg("Słowniki można tworzyć na różne sposoby:"))
print(prg("1. slownik = {}\n   slownik['klucz'] = 'wartość'"))
print(prg("2. slownik = {\n   'klucz1': 'wartość1',\n   'klucz2': 'wartość2'\n}"))
print(prg("3. my_dict = dict(klucz1='wartość1', klucz2='wartość2')"))
print(prg("4. my_list = [('klucz1', 'wartość1'), ('klucz2', 'wartość2')]\n   my_dict = dict(my_list)"))
