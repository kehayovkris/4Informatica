#In ogni riga cerca una parola inserita in input
#e calcola il numero di volte in cui si presenta in ciascuna riga


cerca=input("inserire la parola da cerare")
letterer=open("lettere.txt","r")
cont=0
for line in letterer:
    s=line.split()
    for el in s:
        if el==cerca:
            cont+=1

print("Il valore"+cerca+"\n Si presenta:"+str(cont)+" Volte")