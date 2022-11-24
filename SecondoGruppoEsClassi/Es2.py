# Costruire una classe contenente i dati anagrafici di una persona: codice, cognome, nome,
# un’informazione booleana che indica se la persona è stata sottoposta ad un’approvazione
# o registrazione in generale, dopo la verifica dei suoi dati. I due metodi importanti
# da inserire nella classe sono mostra che rende visibili i dati anagrafici della persona
# e registra che verifica se la persona è stata registrata. Rendere tutti dati visibili solo alla classe,
# rispettando l’incapsulamento. Creare un metodo main in cui si stanziano più oggetti della classe appena
# creata, inserendoli all’interno di una struttura dati a piacere e richiamare attraverso diverse ricerche
# i metodi inseriti nella classe.#
import random


class Persona:
    codice = 0
    nome = ""
    cognome = ""
    b = False

    def __init__(self):
        codice = int(input("Inserisci codice"))
        nome = input("Inserisci nome")
        cognome = input("Inserisci cognome")

    def mostra(self):
        print("codice: " + str(self.codice))
        print("nome: " + self.nome)
        print("cognome: " + self.cognome)

    def registra(self):
        if not self.b:
            return False
        else:
            return True

def main():
    r=random.randint(0,10)
    l=[]
    for i in range(r):
        p=Persona()
        l.append(p)

    while True:
        o=int(input("Selezionare operazione \n 1:inizializza nuopva persona e aggiungi alla strurttura dati \n 2:visualizza informazioni di una persona \n 3: visualizza se la persona è registrata"))
        if o==1:
            pp=Persona()
            l.append(pp)
        elif o==2:
            by=input("Indicare se vuoi cercare tramite \n nome \n cognome \n codice").lower
            if by != "nome" or by != "cognome" or by != "codice":
                print("formato non consetito")
            if by=="nome":
                nome=input("Inserisci nome")
                for p in l:
                    if p.nome==nome:
                        p.mostra()
            elif by=="cognome":
                cognome = input("Inserisci cognome")
                for p in l:
                    if p.cognome == cognome:
                        p.mostra()
            elif by=="codice":
                codice = int(input("Inserisci codice"))
                for p in l:
                    if p.codice == codice:
                        p.mostra()
        elif o==3:
            by = input("Indicare se vuoi cercare tramite \n nome \n cognome \n codice").lower
            if by != "nome" or by != "cognome" or by != "codice":
                print("formato non consetito")
            if by == "nome":
                nome = input("Inserisci nome")
                for p in l:
                    if p.nome == nome:
                        print(p.registra())
            elif by == "cognome":
                cognome = input("Inserisci cognome")
                for p in l:
                    if p.cognome == cognome:
                        print(p.registra())
            elif by == "codice":
                codice = int(input("Inserisci codice"))
                for p in l:
                    if p.codice == codice:
                        print(p.registra())
