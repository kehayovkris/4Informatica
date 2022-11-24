#Determinare il numero di parole diverse contenute in un file di testo.
#Scrivere un programma che legga il testo da un file e determini il numero di parole diverse in esso contenute.


#creazione file stringhe
stringhe=open("stringhe.txt","w")
lent=int(input("Quante parole vuoi inserire all'interno del file"))
for i in range(lent):
    name=input("Inserisci parola")
    stringhe.write(name+ "\n")

#conta numero parole diverse
scr=open("stringhe.txt","r")
cont=0
for line in scr:
    s=line.split()
    for i in range(len(s)):
        if s[i]!= s[i+1] and not s:
            cont+=1



