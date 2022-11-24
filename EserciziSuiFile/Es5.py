def nChar(name):
    testo = open(name, "r")

    r = testo.readline()
    r = r.rstrip()
    count = 0

    while r != "":
        for i in r:
            if i != " ":
                count += 1
        r = testo.readline()
        r = r.rstrip()

    print("Il numero di caratteri è:"+str(count))
    testo.close()


def nWord(name):
    testo = open(name, "r")
    r = testo.readline()
    r = r.rstrip()
    count = 0

    while r != "":
        l = r.split()
        count += len(l)
        r = testo.readline()
        r = r.rstrip()

    print("Il numero di parole è:"+ str(count))
    testo.close()


def nLine(name):
    testo = open(name, "r")
    r = testo.readlines()

    print("Il numero di righe è:"+str(len(r)))
    testo.close()


def main():
    nome = input("Inserisci nome file :")

    t = open(nome, "w")
    n = int(input("Inserisci numero di righe per il file:"))

    for i in range(n):
        r = input("insersci riga:")
        t.write(r)

    t.close()
    nChar(nome)
    nWord(nome)
    nLine(nome)


main()