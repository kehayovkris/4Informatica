#Crea un nuovo file da lettere.txt, letteremaiuscole.txt che contenga
# tutte le righe del file lettere in cui le parole sono trasformate
#tutte in lettere maiuscole e visualizzare il risultato

letteremaiuscole=open("letteremaiuscole.txt","w")
lettere=open("lettere.txt","r")

for line in lettere:
    s=line.split()
    for el in s:
        letteremaiuscole.write(el.upper())

lettere.close()
lmr=open("letteremaiuscole.txt","r")
print(lmr.read())





