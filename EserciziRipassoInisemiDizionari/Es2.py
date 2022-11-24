#Dato il seguente dizionario: Voti={“A” : 8, “D” : 3; “B”: 15, “F”: 2, “C” : 6} scrivere le funzioni che calcolino i seguenti risultati:
#Visualizzare tutte le chiavi
#Visualizzare tutti i valori
#Visualizzare tutte le coppie chiave/valore
#Visualizzare tutte le coppie chiave/valore con le chiavi ordinate
#Calcolare e visualizzare il valore medio
#Visualizzare un diagramma simile al seguente dove ogni riga contiene una chiave seguita da un numero di asterischi uguale al valore associato alla chiave; le righe devono essere visualizzate in ordine di chiave, come nell’esempio:
#A: ********
#B: ***************
#C: ******
#D: ***

def view_key(voti):
    for key in voti.keys():
        print(key)

def view_value(voti):
    for value in voti.values():
        print(value)


def view_keyvalue(voti):
    for key,value in voti.items():
        print(key,value)


def view_sortedKey(voti):
    for key,value in sorted(voti.items()):
        print(key,value)

def view_average(voti):
    s=0
    for value in voti.values():
        s+=value
    return s


def new_dict(voti):
    dict={}
    ast=[]
    for key,value in voti.items():
        for i in range(voti[key]):
            ast.append("*")
        dict[key]=ast
    return dict

def main():
    voti={"A":8,"D" : 3, "B": 15, "F": 2, "C" : 6}
    view_key(voti)
    view_value(voti)
    view_keyvalue(voti)
    view_sortedKey(voti)
    av=view_average(voti)
    di=new_dict(voti)





