#Creare la classe Atleta per rappresentare le informazioni su un giocatore,
# la classe deve contenere un attributo booleano chiamato visitaMedica.
# La classe dovrà contenere i seguenti metodi: metodo che assegni all’atleta il nome della squadra dove gioca,
# un metodo effettua visita che ponga l’attributo visitaMedica uguale a True,
# un metodo che visualizzi i dati del giocatore. Creare un metodo main per provare oggetti di tipo Atleta,
# usando le strutture dati più idonee.#
from random import  random


class Atleta:
    visitaMedica=False
    squadra=""


    def __init__(self):
        self.visitaMedica=False
        self.squadra=""


    def assegnaSquadra(self):
        self.squadra=input("Inserisci il nome della squadra")

    def effettuaVisita(self):
        self.visitaMedica=True

    def view(self):
        print("Il nome della squadra in cui gioca è"+self.squadra)
        print("Lo stato della visita medica è"+str(self.visitaMedica))

def main():
    r=random.randint(0,10)
    l=[]
    c=0
    for i in range(r):
        a=Atleta()
        l.append(a)
    while c==0:
        o=int(input("Seleziona operazione: \n 1:inserire nuovo atleta \n 2: visualizzare squadra \n 3:visualizzare stato visita"))
        if o==1:
            aa = Atleta()
            l.append(aa)
        elif o==2:
            for a in l:
                print(a.squadra)
        elif o==3:
            for a in l:
                print(a.visitaMedica)


