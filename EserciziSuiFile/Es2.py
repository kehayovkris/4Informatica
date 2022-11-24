def agg():
    t = open("testo.txt", "r")
    new = open("new.txt", "w")
    riga = t.readline()
    riga = riga.rstrip()
    count = 0

    while riga != "":
        count += 1
        new.write("/* {c} */ {r}\n".format(c=count, r=riga))
        riga = t.readline()
        riga = riga.rstrip()

    new.close()
    t.close()


def main():
    testo = open("testo.txt", "r+")
    n = int(input("Inserisci numero di righe per il file:\n"))

    for i in range(n):
        riga = input("insersci riga:")
        testo.write("{}\n".format(riga))

    testo.close()
    agg()


main()

