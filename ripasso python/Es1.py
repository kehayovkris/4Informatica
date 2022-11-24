#Molti siti web e pacchetti software chiedono agli utenti di creare password che contengano almeno una cifra e un carattere speciale.
# Il vostro compito è quello di scrivere un programma che generi una tale password, che abbia, inoltre, la lunghezza specificata
# scegliendo caratteri a caso'
import string
import random

def generaPassCasuale(len):
    chars= string.ascii_letters+"0123456789"+"!£$%&/()=*|é*°-_,.§"
    password= "".join((random.choice(chars) for i in range(len)))
    return password
    
len=int(input("Inserisci la lunghezza della password che vuoi generare"))
print(generaPassCasuale(len))