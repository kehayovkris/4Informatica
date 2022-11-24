# Scrivere un programma che legga un file contenente stringhe di parole e le inserisca in un insieme.
# Il programma deve riscrivere il file letto generandone un altro nel quale tutte le lettere delle parole
# che iniziano con le lettere CA siano sostituite da asterischi.


# INIZIALIZZO IL PRIMO FILE E L'INSIEME
stringhe = open("stringhe.txt", "w")
s = set()
lent = int(input("Quante parole vuoi inserire all'interno del file"))
for i in range(lent):
    name = input("Inserisci parola")
    s.add(name)
    stringhe.write(name + "\n")

# CREAZIONE DEL SECONDO FILE
sca = open("stringheCa.txt", "w")
sr = open("stringhe.txt", "r")

line = sr.readline()
for line in sr:
    s = line.split()
    for el in s:
        if el[0] == "c" or "C" and el[1] == "a" or "A":
            for i in range(len(el)):
                el[i] = "*"


