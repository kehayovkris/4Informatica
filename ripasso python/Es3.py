from random import random


def lanciadado():
    len=int(input("Inserisci quante volte vuoi lanciare il dado"))
    lanci=[]
    for i in range(len):
        lanci.append(random.randint(1,6))
    return lanci


def calcola(lanci):
    one=0
    two=0
    three=0
    four=0
    five=0
    six=0
    for i in range(len(lanci)):
        if lanci[i] == 1:
            one + 1
        elif lanci[i] == 2:
            two + 1
        elif lanci[i] == 3:
            three + 1
        elif lanci[i] == 4:
            four + 1
        elif lanci[i] == 5:
            four + 1
        elif lanci[i] == 6:
            four + 1
    print("ci sono" + str(one) + "volte i numeri 1" + "ci sono" + str(two) + "volte i numeri 2" + "ci sono" + str(
    three) + "volte i numeri 3" + "ci sono" + str(four) + "volte i numeri 4" + "ci sono" + str(
    five) + "volte i numeri 5" + "ci sono" + str(six) + "volte i numeri 6")


d=lanciadado()
calcola(d)
