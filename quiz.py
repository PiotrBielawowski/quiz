import keyboard
import time
import random

zagadka = [
    {"pytanie": "Jaki typ danych przechowuje liczby całkowite?", "odp": "A - integer \nB - float \nC - string \nD - bool", "podp": "a"},
    {"pytanie": "Jaki typ danych przechowuje liczby zmiennoprzecinkowe?", "odp": "A - integer \nB - float \nC - string \nD - bool", "podp": "b"},
    {"pytanie": "Jak ma na imię autor quizu?", "odp": "A - Mateusz \nB - Wojtek \nC - Piotr \nD - Michał", "podp": "c"},
    {"pytanie": "Jaki jest obecny rok kalendarzowy?", "odp": "A - 2025 \nB - 2014 \nC - 2024 \nD - 1990", "podp": "a"},
    {"pytanie": "W którym roku była bitwa pod grunwaldem?", "odp": "A - 966 \nB - 1939 \nC - 1410 \nD - 1510", "podp": "c"},
    {"pytanie": "Jak nazywa się obecny prezydent Stanów Zjednoczonych?", "odp": "A - Donald Trump \nB - Donald Tusk \nC - Joe Reagan \nD - George Washington", "podp": "a"},
    {"pytanie": "Czy 2/5 jest większe od 40%?", "odp": "A - Tak \nB - Nie", "podp": "b"}
]
random.shuffle(zagadka)

numer_pytania = 0

print("Aby odpowiadać na pytania używaj klawiszy A, B, C, D - Quiz Wykonał Piotr Bielawowski")
for quiz in zagadka:
    print(quiz["pytanie"])
    print(quiz["odp"])
    
    odp = None
    while True:
        if keyboard.is_pressed("a") or keyboard.is_pressed("A"):
            odp = "a"
            time.sleep(0.2)
            break
        elif keyboard.is_pressed("b") or keyboard.is_pressed("B"):
            odp = "b"
            time.sleep(0.2)
            break
        elif keyboard.is_pressed("c") or keyboard.is_pressed("C"):
            odp = "c"
            time.sleep(0.2)
            break
        elif keyboard.is_pressed("d") or keyboard.is_pressed("D"):
            odp = "d"
            time.sleep(0.2)
            break

    if odp == quiz["podp"]:
        print("Dobrze! To jest poprawna odpowiedź")
        numer_pytania = numer_pytania + 1
    else:
        print("Ta odpowiedź jest niepoprawna! Poprawna odpowiedź to: ", quiz["podp"])
        numer_pytania = numer_pytania 
        break

print("Koniec quizu! Twój wynik to: ", numer_pytania, " na ", len(zagadka), "punktów")
if numer_pytania == len(zagadka):
    print("Gratulacje! Odpowiedziałeś poprawnie na wszystkie pytania!")
else:
    print("Niestety nie udało Ci się zdobyć maksymalnej liczby punktów, poćwicz i wykonaj ten quiz jeszcze raz!")



