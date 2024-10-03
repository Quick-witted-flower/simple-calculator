import logging

logging.basicConfig(level=logging.INFO)

def dodawanie(a, b):
    logging.info(f'Dodaję {a} i {b}')
    return a + b

def odejmowanie(a, b):
    logging.info(f'Odejmuję {b} od {a}')
    return a - b

def mnozenie(a, b):
    logging.info(f'Mnożę {a} przez {b}')
    return a * b

def dzielenie(a, b):
    if b != 0:
        logging.info(f'Dzielę {a} przez {b}')
        return a / b
    else:
        logging.info('Błąd: Próba dzielenia przez zero')
        return "Błąd: Dzielenie przez zero"

def main():
    
    print("Podaj działanie, posługując się odpowiednią liczbą:")
    print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    operacja = input()

    
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    
    if operacja == '1':
        wynik = dodawanie(liczba1, liczba2)
    elif operacja == '2':
        wynik = odejmowanie(liczba1, liczba2)
    elif operacja == '3':
        wynik = mnozenie(liczba1, liczba2)
    elif operacja == '4':
        wynik = dzielenie(liczba1, liczba2)
    else:
        wynik = "Nieprawidłowy wybór"

    
    print(f"Wynik to: {wynik}")


main()

