#Creare un file che contenga almeno 5 righe nominandolo con lettere.txt,
# ogni riga deve contenere spazi, caratteri come ; : ? !

lettere=open("lettere.txt","w")

for i in range(5):
    name=input("Inserisci il tuo nome")
    age=input("Inserisci eta")
    lettere.write("Ciao, mi chiamo: "+name+"\n La mia èta è :"+age+"!")

letterer=open("lettere.txt","r")
print(letterer.read())
lettere.close()




