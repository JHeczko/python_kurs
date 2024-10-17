line = "Ala ma kota\nKot ma ale\tale niekoniecznie kot jest w posiadaniu ali\nThe end\nGvR"
word = "Jakiswyrazdlugi"
L = [1,213,12,32,2,123,12,5,32]
big_int = 101230049103402130421300000234021

# ZADANIE 2.10
# Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. 
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).
print("=== ZADANIE 2.10 ===")
print("Liczba wyrazów w napisie:", line.split().__len__())

# ZADANIE 2.11
# Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.
print("\n=== ZADANIE 2.11 ===")
print('_'.join(word))

# ZADANIE 2.12
# Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. 
# Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
print("\n=== ZADANIE 2.12 ===")
print(" ".join(line.split()[0:3]), line.split()[-1], sep=' | ')

# ZADANIE 2.13
# Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().
print("\n=== ZADANIE 2.13 ===")
print("Łączna długość wyrazów w napisie:", sum(len(word) for word in line.split()))

# ZADANIE 2.14
# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
print("\n=== ZADANIE 2.14 ===")
print(max(line.split(), key=len), max(len(word) for word in line.split()), sep=' | Długość słowa: ')

# ZADANIE 2.15
# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
print("\n=== ZADANIE 2.15 ===")
print(''.join(map(str,L)))

# ZADANIE 2.16
# W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".
print("\n=== ZADANIE 2.16 ===")
print(repr(line.replace('GvR', 'Guido van Rossum')))

# ZADANIE 2.17
# Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. 
# Wskazówka: funkcja wbudowana sorted().
print("\n=== ZADANIE 2.17 ===")
sorted_list = line.split()
sorted_list.sort()
print("Posortowane alfabetycznie:", sorted_list)
sorted_list.sort(key=len)
print("Posortowane według długości:", sorted_list)

# ZADANIE 2.18
# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.
print("\n=== ZADANIE 2.18 ===")
print("Liczba cyfr '0' w dużej liczbie:", str(big_int).count('0'))

# ZADANIE 2.19
# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. 
# Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. 
# Wskazówka: str.zfill().
print("\n=== ZADANIE 2.19 ===")
print(', '.join(map(lambda x: str(x).zfill(3), L)))
