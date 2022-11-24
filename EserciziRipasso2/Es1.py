# Per ciascuna delle operazioni elencate sotto, scrivere la funzione corrispondente e richiamare
# ciascuna nel metodo main:
# Inserire n elementi numerici in una lista
# Ordinare gli elementi in ordine decrescente
# Visualizzare tutti gli elementi, separati da una stringa inserita in input
# Contare quanti elementi della lista sono minori di un elemento inserito in input
# Eliminare tutti gli elementi che sono minori di un valore dato in input
# Copiare in un’altra lista tutti gli elementi che sono maggiori di un elemento dato in input
# Visualizzare la tabella
# Creare un metodo main dove richiamare tramite un menù tutte le operazioni precedenti


def inizializza():
    n=int(input("Inserisci il numero di elementi che vuoi inserire"))
    l=[]
    for i in range(n):
        l.append(int(input("Inserisci numero")))
    return l

def decrescente(l):
    return reversed(l)

def separati_stringa(l):
    l1=[]
    s=input("Inserisci stringa")
    for el in l:
        l1.append(el)
        l1.append(s)
    return l1

def conta(l):
    n= int(input("Inserisci numero"))
    cont=0
    for el in l:
        if n>el:
            cont+=1
    return cont

def elimina(l):
    n= int(input("Inserisci numero"))
    for el in l:
        if el < n:
            l.remove(el)

def newList(l):
    n= int(input("Inserisci numero"))
    l1=[]
    for el in l:
        if el>n:
            l1.append(el)
    return l1

def tabella(l,l1):
    tab=[l]
    tab.append(l1)
    return tab

def view(l):
    for el in l:
        print(el)


def main():
    l= inizializza()
    print("Lista Inizializzata:")
    view(l)

    ld=decrescente(l)
    print("Lista decrescente:")
    view(ld)

    l1= separati_stringa(l)
    print("Lista con i separati da una stringa")
    view(l1)

    cont=conta(l)
    print("Contatore numeri minori di n"+ str(cont))


    elimina(l)
    print("Elimina elementi minori di n")
    view(l)


    l2=newList(l)
    print("Nuova lista con elementi maggiori di n")
    view(l2)

    tab=tabella(l,l2)
    print("Visualizza tabella")
    view(tab)

main()











