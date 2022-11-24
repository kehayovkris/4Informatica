import os


def initialize():
    s = open("studenti.txt", "r")
    n = open("informazioni.txt", "w")
    for line in s:
        l = line.split()
        p = l[0] + " " + input("Insersci lingua") + " " + input("Insersci ore") + "\n"
        n.write(p)
    s.close()
    n.close()

def view():
    n = open("informazioni.txt", "r")
    for line in n:
        print(line)
    n.close()

def cambiaore():
    n = open("informazioni.txt", "r")
    s = open("info.txt", "w")
    lin = input("Inserisci lingua per cui si vuole modificare le ore").lower()
    ore = int(input("Inserisci numero di ore da sommare: "))
    line = n.readline()
    line = line.rstrip()

    while line != "":
        l = line.split()
        if l[1] == lin:
            ore += int(l[2])
            s.write("{} {} {}\n".format(l[0], l[1], str(ore)))
        else:
            s.write("{}\n".format(line))
        line = n.readline()
        line = line.rstrip()
    s.close()
    n.close()

def average():
    s = open("info.txt", "r")
    lin=input("Inserisci lingua per vedere la media delle ore")
    sum=0
    cont=0
    for line in s:
        l=line.split()
        if l[1]== lin:
            sum+=l[2]
            cont+=1
    return sum/cont

def main():
    initialize()
    view()
    b=True
    while b:
        choice=int(input("selezionare operazione \n 1:aggiungere ore scegliendo la lingua"
                     "\n 2:La medie delle ore effettuate per ogni lingua \n "))
        if choice==1:
            cambiaore()
            view()
        elif choice==2:
            print("La media è"+str(average()))
        else:
            print("Richiesta non presente")

main()
