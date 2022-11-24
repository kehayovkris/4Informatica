def initialize():
    r = open('school.txt',"r")
    w=open("class.txt","w")
    for line in r:
        w.write(line+input("Inserisci la classe"))

def view():
    r=open("class.txt","r")
    for line in r:
        print(line)

def count():
    r = open("class.txt", "r")
    count=0
    for line in r:
        line.rstrip()
        if input("Inserisci classe") in line:
            count+=1
    return count

def classBySur():
    r = open("class.txt", "r")
    s=[]
    for line in r:
        line.rstrip()
        if input("Inserisci cognome") in line:
            s=line.split()
    return s[2]

def sameName():
    r = open("class.txt", "r")
    l=[]
    for line in r:
        line.rstrip()
        if input("Inserisci nome") in line:
            s=line.split()
            l.append(s)
    return l
def main():
    initialize()
    view()
    o=0
    c = input("Vuoi eseguire qualche operazione y=si n=no") == "y"
    while c=="y":
        try:
            o=int(input("Premi \n 1:Per contare gli studenti di una classe indicata "
                "\n 2:Visulizzare la classe inserendo il cognome "
                "\n 3:visualizzare informazioni di tutti quelli con lo stesso nome"
                "\n 4:Visualizzare il file"))
            if o>5:
                print("operazione non presente")
        except ValueError:
            print("Inserisci numero")
        if o==1:
            c=count()
            print("Ci sono"+str(c)+"studenti peer la classe indicata")
        elif o==2:
            c=classBySur()
            print("La classe dello studente indicato è"+c)
        elif o==4:
            view()
main()
