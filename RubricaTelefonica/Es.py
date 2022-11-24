import os
import pickle
import pickle as serializer

# Classe contatto che servira per serializzare un oggetto (.ct)
import time


class Contact:
    def __init__(self, nam, sur, num):
        self.name = nam
        self.surname = sur
        self.number = num


# Funzione che crea un file .ct inizializzando un contatto
def create_contact():
    na = input("Inserisci nome")
    with open("contacts/" + na + ".ct", "wb") as outfile:
        serializer.dump(Contact(na, input("Inserisci cognome"), validate_number()), outfile,
                        pickle.HIGHEST_PROTOCOL)


# Funzione che permette all'utente di inserire il numero telefonico dell'utente verificando le eccezioni probabili
def validate_number():
    n = ""
    try:
        n = input("Inserisci numero")
        if not len(n) == 10:
            _x = 1 / 0  # Ene non aveva voglia di capire come si lanciano eccezioni in python
    except ValueError:
        print("Puoi inserire solo numeri ")
        validate_number()
    except ZeroDivisionError:
        print("Formato non consentito")
        validate_number()
    return str(n)


def open_f(file):
    c = None
    try:
        c = serializer.load(file)
    except EOFError:
        print("Failed to open file, retrying in 1 second")
        time.sleep(1000)
        open_f(file)
    return c


def search(sea, ty, change):
    for file in os.listdir("contacts"):
        with open("contacts/" + file, "rb+") as f:
            c: Contact = open_f(f)
            if ty == "sur":
                if c.surname == sea:
                    print(c.surname, c.name, c.number)
                    if change:
                        c.number = validate_number()
                        print("new num" + str(c.number))

            elif ty == "nam":
                if c.name == sea:
                    print(c.surname, c.name, c.number)
            elif ty == "num":
                if c.number == sea:
                    print(c.surname, c.name, c.number)

            f.close()
        serializer.dump(c, open("contacts/" + file, "wb"), pickle.HIGHEST_PROTOCOL)


# Funzione main che lancia il programma attraverso DUE cicli while per gestire le operazioni
def main():
    c = input("Vuoi aggiungere contatti? y:Si, n:No") == "y"
    f = True
    while c:
        create_contact()
        if input("Vuoi inserire un altro contatto? \n y:Si n:No") == "n":
            c = False
    while f:
        typ = input("Che tipo di ricerca? num, nam, sur")
        search(input("Input cosa cercare"), typ, input("cambia numero? y:si, n: no") == "y")
        f = input("Vuoi fare un altra operazione? \n y:Si n:No") == "y"


main()
