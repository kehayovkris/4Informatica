from NoleggioAuto import *
from NoleggioCamper import *
def main():
    listaNoleggi=[]
    continua=1
    while continua==1:
        operazione=int(input("Seleziona l'operazione \n 1:aggiungere un nuovo noleggio  \n 2:visualizzare informazioni del noleggio \n 3:modifica durata noleggio"))
        if operazione==1:
            noleggia(listaNoleggi)
        elif operazione==2:
            info=int(input("Seleziona info da visualizzare: \n 1: giorni di noleggio \n 2: tariffa applicata \n 3: prezzo totale  \n  4:tutte le informazioni presenti"))
            n=input("inserisci il nome del noleggiatore")
            if info==1:
                for el in listaNoleggi:
                    if el.getnome==n:
                        print(el.getgiorni())
            elif info==2:
                for el in listaNoleggi:
                    if el.getnome==n:
                        print(el.gettariffa())
            elif info == 3:
                for el in listaNoleggi:
                    if el.getnome==n:
                        print(el.getprezzo())
            elif info==4:
                for el in listaNoleggi:
                    if el.getnome==n:
                        el.__str__()
        elif  operazione==3:
            n = input("inserisci il nome del noleggiatore")
            giorniExtra=int(input("Inserire il numero di giorni extra"))
            for el in listaNoleggi:
                if el.getnome()==n:
                    el.setgiorni(giorniExtra)
                    el.calcolaprezzo()
        else:
            print("Non e stata trovata nessuna operazione corrispondente")

    continua=int(input("Premere 1 per continuare 0 per terminare"))

def noleggia(l):
    nome = input("Inserire il nome del noleggiante")
    noleggio = int(input("Premere \n 1: per noleggiare un auto \n 2: per noleggiare un camper"))
    if noleggio == 1:
        na=NoleggioAuto()
        na.setnome(nome)
        giorni=int(input("Inserire la durata del noleggio espressa in giorni"))
        na.setgiorni(giorni)
        na.calcolaprezzo()
        l.append(na)
    elif noleggio==2:
        nc=NoleggioCamper()
        nc.setnome(nome)
        giorni = int(input("Inserire la durata del noleggio espressa in giorni"))
        nc.setgiorni(giorni)
        nc.calcolaprezzo()
        l.append(nc)


main()