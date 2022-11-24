#Eliminare da ciascuna riga tutti gli spazi che si trovano a sinistra ed eliminare tutti i caratteri
# ; : ? ! che si trovano a destra.
# Per ogni riga conta il numero delle parole presenti e il numero caratteri presenti.

lettere=open("lettere.txt","r")

contP=0
contC=0
for line in lettere:
    s = line.split()
    contP = contP + len(s)
    line.rstrip(";:?!")
    for el in s:
        for l in el:
            contC+=1


print("la conta delle parole è" + str(contP))
print("la conta dei caratteri è" + str(contC))







