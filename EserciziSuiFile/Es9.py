def sort():
    rev = open("reverse.txt")
    newr = open("newReverse.txt", "w")

    r = rev.readlines()

    for i in range(len(r), 0, -1):
        newr.write(r[i - 1].rstrip())

    rev.close()
    newr.close()


def main():
    rev = open("reverse.txt", "w")
    b = False

    while True:
        r = input("Inserisci riga o digita 0 per finire l'inserimento: ")
        if  r == "0" and b == True:
            break
        elif  r == "0" and b == False:
            exit()
        else:
            rev.write(r)
            b = True

    rev.close()
    sort()

main()