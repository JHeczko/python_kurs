def prg(skk): return ("\033[92m {}\033[00m" .format(skk))
def prr(skk): return ("\033[91m {}\033[00m" .format(skk))

# ZADANIE 3.4
# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
while True:
    try:
        x = input(prg("Podaj liczbę rzeczywistą: "))
        if x == 'stop':
            print(prg("Stopping program action..."))
            exit(0)
        else:
            print(pow(float(x),3))
    except ValueError:
        print(prr('[ERROR] '),"To nie jest liczba")