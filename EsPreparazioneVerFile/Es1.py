#Scrivi un programma per registrare in un file di testo i nomi delle province di una regione italiana.
# Leggi il contenuto del file creato scaricando i dati in una lista di stringhe.
# Visualizza poi l’elenco ordinato delle città.
# Conta quante righe contiene il file di testo,
# dopo aver controllato che tale file è presente nella memoria.#



def inizializza():
    f=open("provincie.txt","w")
    ins=""
    while ins != "0":
        ins=input("Inserisci nome provincia")
        f.write(ins)

def leggi(nome):
    f=open(nome,"r")
    f.readline()
    lis=[]
    for line in f:
        l=line.split()
        lis.append(l)
    return lis

def sorted(nome):
    pass