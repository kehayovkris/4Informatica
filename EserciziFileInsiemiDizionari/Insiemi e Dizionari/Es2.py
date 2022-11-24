#Scrivere un programma che legga un file di testo, converta tutte le sue parole in minuscolo e
# visualizzi tutte quelle che contengono le lettera a, poi tutte quelle che contengono la lettera b e così via.
# Costruire un dizionario le cui chiavi siano le lettere minuscole e i cui valori siano insiemi di parole
# che contengono una determinata lettera

#creazione file stringhe convertendo in minuscolo
stringhe=open("stringhe.txt","w")
len=int(input("Quante parole vuoi inserire all'interno del file"))
for i in range(len):
    name=input("Inserisci parola")
    stringhe.write(name.lower()+ "\n")

#visualizzi tutte quelle che contengono a b e cosi via
stc=open("stringhe.txt","r")
a=set()
b=set()
c=set()
d=set()
for line in stc:
    s=line.split()
    for el in s:
        if el[0]=="a"or "A":
            print(el)
            a.add(el[0])
        if el[0] == "b" or "B":
            print(el)
            b.add(el[0])
        if el[0] == "c" or "C":
            print(el)
            c.add(el[0])
        if el[0] == "d" or "D":
            print(el)
            d.add(el[0])
#costruisci dizionario
dict={}
keys=["a","b","c","d"]
values=[a,b,c,d]
for i in range(4):
    dict[keys[i]]=values[i]

#visualizza dizionario
for key,value in dict.items():
    print(key,value)






