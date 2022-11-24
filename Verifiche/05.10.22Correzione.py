import  random
import string

" FUNZIONI RICHIESTA 1"
def inserisciRandom():
    l=[]
    len=int(input("Quanti numeri casuali vuoi inserire?"))
    for i in range(len):
        l.append(random.randint(2,10000))
    return l

def viewlist(l):
    for el in l:
        print(el)

def eliminaMultipli(l):
    for el in l:
        if el%3==0 or el%5==0:
            l.remove(el)

def secondoMax(l):
    l1=l
    for el in l1:
        if el==max(l1):
            l1.remove(el)
    return str(max(l1))

def sostiuisci(l):
    for i in range(0,len(l),2):
        l[i]=0

"FUNZIONI RICHIESTA 2"
def inizializzaTabella(m,n):
    tab = []
    for i in range(m):
        l = []
        for j in range(n):
            l.append(0)
            tab.append(l)
    return tab

def viewmatrix(tab,m):
    for el in tab:
        for i in range(m):
            print(el[i])

def unoPari(tab,m,n):
    for i in range(m):
        for j in range(n):
            if j % 2 == 0:
                tab[i][j]=1

def dueDispari(tab,m,n):
    for i in range(m):
        for j in range(n):
            if j % 2 != 0 and i % 2 != 0:
                tab[i][j] = 2


def somma(m,tab):
    sum=0
    for el in tab:
        for i in range(m):
            sum+=el[i]
    return sum


"FUNZIONI RICHIESTA 3"
def caricaStringaCasuale():
    n=random.randint(0,20)
    for i in range(n):
        s1=random.choice(string.ascii_letters)
    return s1

def insiememinuscole(s1):
    min=set(string.ascii_lowercase)
    for l in s1:
        if l in min:
            min.remove(l)
    return min

def viewset(min):
    for el in min:
        print(el)

def dizionarioOccorrenze(s1):
    dict={}
    keys=[string.ascii_letters]
    for key in keys:
        dict[key]=0
    for key,value in dict.items():
        for el in s1:
            if key==el:
                value=value+1
    return dict

def viewdict(dict):
    for key,value in dict.items():
        print(key,value)

def maxOccorrenza(dict):
    return max(dict.values())

def minOccorrenza(dict):
    return min(dict.values())


def main():
    t=True
    def continua(t):
        c=input("Premere 1 per continuare 0 per uscire")
        if c==1:
            t=True
        elif c==0:
            t=False
            exit()
        else:
            print("Errore")
    while t:
        richiesta=int(input("Selezionare richiesta: \n Premere 1 2 o 3"))
        if richiesta==1:
            l=inserisciRandom()
            viewlist(l)
            eliminaMultipli(l)
            viewlist(l)
            print("Il secondo valore maggiore è"+secondoMax(l))
            sostiuisci(l)
            viewlist(l)
            continua(t)
        elif richiesta==2:
            m = int(input("Inserisci numero di righe"))
            n = int(input("Inserisci numero di colonne"))
            tab=inizializzaTabella(m,n)
            viewmatrix(tab,m)
            unoPari(tab,m,n)
            viewmatrix(tab,m)
            dueDispari(tab,m,n)
            viewmatrix(tab,m)
            print("La somma è"+str(somma(m,tab)))
            continua(t)
        elif richiesta==3:
            s1=caricaStringaCasuale()
            insieme=insiememinuscole(s1)
            viewset(insieme)
            occ=dizionarioOccorrenze(s1)
            viewdict(occ)
            print("Il valore massimo è" + str(maxOccorrenza(occ)))
            print("Il valore massimo è" + str(minOccorrenza(occ)))
            continua(t)
        else:
            print("Errore")
            continua(t)


main()

