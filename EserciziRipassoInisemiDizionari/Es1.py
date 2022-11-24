#Scrivere una funzione che riceve come argomenti due stringhe e restituisca:
#un insieme contenente le lettere maiuscole e minuscole che sono presenti in entrambe le stringhe
#Un insieme contenente le lettere maiuscole e minuscole che non sono presenti in alcuna stringa
#Un insieme contenente i caratteri che non sono lettere e che sono presenti in entrambe le stringhe


def maiuscoleMinuscole(s1,s2):
    s=set()
    for l in s1,s2:
        s.add(l)
    return s

def nonPresenti(s1,s2):
    s=set()
    minuscolo="abcdefghijklmnopqrstuvwxyz"
    maiuscolo="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for l in s1,s2:
        if l not in minuscolo:
            s.add(l)
        if l not in maiuscolo:
            s.add(l)
    return s

def nonLettere(s1,s2):
    s=set()
    minuscolo="abcdefghijklmnopqrstuvwxyz"
    maiuscolo="ABCDEFGHIJKLMNOPQRSTUVWXYZ"





