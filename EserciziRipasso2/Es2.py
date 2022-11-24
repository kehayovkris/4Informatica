#Scrivere un programma che i risolvi i seguenti problemi, ciascuno risolto con una funzione, relativi
#ad una tabella quadrata di m righe ed m colonne:
#Riempire inizialmente la tabella con tutti 0
#Riempire la tabella con tutti 1
#Scrivere nelle caselle della tabella alternativamente 0 e 1, secondo uno schema a scacchiera
#Scrivere il valore 0 in tutte le caselle della prima riga e dell’ultima
#Scrivere il valore 1 in tutte le caselle delle colonne di posizione pari
#Calcolare la somma di tutti gli elementi
#Visualizzare la tabella
#Creare un metodo main dove richiamare tramite un menù tutte le operazioni precedenti

def inizializza0(righe, colonne):
    tab = []
    for i in range(righe):
        l = []
        for j in range(colonne):
            l.append(0)
        tab.append(l)
    return tab


def inizializza1(righe, colonne):
    tab = []
    for i in range(righe):
        l = []
        for j in range(colonne):
            l.append(1)
        tab.append(l)
    return tab

def scacchiera(righe,colonne,tab):
    verify = True
    for i in range(righe):
        l = []
        for j in range(colonne):
            if verify == True:
                l.append(0)
                verify = False
            elif verify == False:
                l.append(1)
                verify = True
        tab.append(l)


def primaUltimaRiga(righe, colonne,tab):
    for i in range(righe):
        l = []
        for j in range(colonne):
            if j == 0 or j == (colonne - 1):
                l.append(0)
            else:
                l.append(1)
        tab.append(l)



def inserisci1Pari(righe, colonne,tab):
    for i in range(righe):
        l = []
        for j in range(1, colonne + 1):
            if j % 2 == 0:
                l.append(1)
            else:
                l.append(0)
        tab.append(l)


def somma(righe,tab):
    sum=0
    for el in tab:
        for i in range(righe):
            sum+=el[i]
    return sum

def view(righe,tab):
    for el in tab():
        for i in range(righe):
            print(el[i])

def main():
    righe = int(input("Inserisci numero righe:"))
    colonne = int(input("Inserisci numero colonne:"))

    tab0=inizializza0(righe, colonne)
    tab1=inizializza1(righe, colonne)

    scacchiera(righe, colonne, tab0)
    view(tab0)
    primaUltimaRiga(righe, colonne, tab0)
    view(tab0)
    inserisci1Pari(righe, colonne, tab0)
    view(tab0)

main()