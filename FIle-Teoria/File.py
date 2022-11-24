#INIZIALIZZAZIONE FILE STRINGHE
stringhe=open("stringhe.txt","w")
len=int(input("Quante parole vuoi inserire all'interno del file"))
for i in range(len):
    name=input("Inserisci parola")
    stringhe.write(name + "\n")

#INIZIALIZZAZIONE FILE NUMERI
stringhe=open("stringhe.txt","w")
len=int(input("Quanti numeri vuoi inserire all'interno del file"))
n=0
for i in range(len):
    try:
        n=int(input("Inserisci numero"))
        stringhe.write(str(n))
    except ValueError:
        print("Inserire numero")
#LETTURA FILE PER RIGHE




#INIZIALIZZAZIONE FILE CSV


