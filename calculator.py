import logging
# Konfiguracja logging, ustawiam poziom na INFO, aby wyświetlić informacje
logging.basicConfig(level=logging.INFO)

# Pytam użytkownika o działanie
operation = input("Podaj działanie, posługując się odpowiednią liczbą : 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

# Pobieram dwie liczby od użytkownika
liczba1 = float(input("Podaj pierwszą liczbę:"))
liczba2 = float(input("Podaj drugą liczbę :"))

# Sprawdzam, jaka operację wybrał uzytkownik i wykonujemy odpowiednie działanie
if operation == '1':
    wynik = liczba1 +liczba2
    logging.info(f"Dodaję {liczba1} i {liczba2}")
elif operation == '2':
    wynik = liczba1 - liczba2
    logging.info(f"Odejmuję {liczba1} i {liczba2}")
elif operation == '3':
    wynik = liczba1 * liczba2
    logging.info(f"Mnożę {liczba1} i { liczba2}")
elif operation == '4':
    if liczba2 != 0:
        wynik = liczba1 / liczba2
        logging.info(f"Dzielę {liczba1} i {liczba2}")
    else:
        wynik = "Błąd : nie można dzielić przez 0!"
        logging.error("Próba dzielenia przez zero")
else:
    wynik = "Błędny wybór operacji!"
    logging.warning("Niepoprawna operacja została wybrana")

# Wyświetlam wynik
print(f"Wynik to : {wynik}")

