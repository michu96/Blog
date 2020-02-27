import random
import requests
import string
from bs4 import BeautifulSoup


def pobierz():
    liczba = int(input("Wpisz liczbe różną od zera: "))
    if liczba != 0:
        return liczba
    else:
        return int(input("Podałeś zero, wpisz inna liczbę: "))


def sprawdzenie(liczba):
    flaga = True
    for x in range(2, liczba):
        if liczba%x == 0:
            flaga = False
            break
    return flaga


def fibona(liczba):
    ciag = [1]
    for x in range(0, liczba - 1):
        if x == 0:
            ciag.append(1)
        else:
            ciag.append(ciag[x - 1] + ciag[x])
    print(ciag)


def odwracanie(text):
    text.strip()
    lista = text.split()
    lista2 = []
    for x in range(len(lista) -1, -1, -1):
        lista2.append(lista[x])
    wynik = " ".join(lista2)
    print(wynik)


def losowanie(len):
    qwerty = "abcdefghijklmnoprstuwxyz0123456789ABCDEFGHIJKLMNOPRSTUWXYZ!@#$%^&*_?"
    haslo = "".join(random.sample(qwerty, len))
    print(haslo)


def cow_bull():
    krowa = 0
    byk = 0
    los = str(random.randint(1000, 9999))
    while krowa != 4:
        wpis = input("Wpisz wartość: ")
        for i in range(4):
            for j in range(4):
                if i == j and los[i] == wpis[j]:
                    krowa += 1
                elif i != j and los[i] == wpis[j]:
                    byk += 1
        print("Wylosowana liczboa to: " + str(los))
        print("Zdobyte krowy: " + str(krowa) + ", zdobyte byki: " + str(byk))
        print(" ")
        krowa = 0
        byk = 0


def pliki_w(nazwa, dane):
    with open(nazwa, "a") as plik:
        plik.write(dane)


def pliki_r(nazwa):
    with open(nazwa, "r") as plik:
        return plik.read()


def main():
    pass


if __name__ == '__main__':
    main()