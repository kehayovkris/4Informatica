def controlla():
    testo = open("testo.txt")
    riga = testo.readline()

    cont = open("controllo.txt")
    rigaCont = cont.readlines()

    contenuta = False

    while riga != "":
        for i in range(len(rigaCont)):
            if riga == rigaCont[i]:
                contenuta = True
        if contenuta == False:
            print("Questa parola non è presente nel file:", riga)
        riga = testo.readline()


def main():
    testo = open("testo.txt", "w")

    n = int(input("Inserisci numero di parole:"))

    for i in range(n):
        p = input("Inserisci parola: ").lower()
        testo.write(p)

    testo.close()
    controlla()


main()