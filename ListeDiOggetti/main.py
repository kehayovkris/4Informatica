from Carta import Carta

def main():
    b=True
    while b:
        c=int(input("Seleziona operazione \n 1:Crea un mazzo di carte \n 2:visualizza colore indicando indice  \n 3:visualizza rango indicando indice  \n 4:visualizza tutte informazioni indicando l'indice \n 5: esci dal programma" ))
        mazzo=[]
        if c==1:
            for c in range(3):
                for r in range(9):
                    u=Carta(c,r)
                    mazzo.append(u)
        elif c==2:
            index=int(input("inserisci indice della carta"))
            if index <= len(mazzo):
                print(mazzo[index].getcolor())
            else:
                print("carta non esistente")
        elif c == 3:
            index = int(input("inserisci indice della carta"))
            if index <= len(mazzo):
                print(mazzo[index].getrango())
            else:
                print("carta non esistente")
        elif c == 4:
            index = int(input("inserisci indice della carta"))
            if index <= len(mazzo):
                print(mazzo[index].getinfo())
            else:
                print("carta non esistente")
        elif c == 5:
            b=False
        else:
            print("operazione non esistente")


