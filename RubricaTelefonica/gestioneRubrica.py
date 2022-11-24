#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 19:05:26 2022

@author: mariaastarita
"""
##Scrivere un programma che gestisca una rubrica telefonica rispettando le seguenti richieste:
# Creare un metodo main che contenga un menu per scegliere le seguenti operazioni:
# Creare una rubrica telefonica con Cognome, Nome e numero di telefono; ordinando il tutto in senso crescente di cognome.
# Aggiungere nuovi nomi alla rubrica
# Visualizzare la rubrica
# Inserire un cognome, effettuare la ricerca del numero di telefono e visualizzare il cognome e il numero corrispondente
# Inserire il numero, effettuare la ricerca del cognome e visualizzare sia il cognome, sia il numero
# Inserire un nome e ricercare tutti i cognomi che hanno quel nome e visualizzare tutte le informazioni della ricerca fatta
# Modificare un numero di telefono, inserendo il cognome
# Ogni operazione del menu deve essere realizzata tramite una funzione che verrà richiamata nel main
import os
def caricaRubrica(nome):
    c="si"
    fileOut=open(nome, "w")
    while c=="si":
        fileOut.write(input("Inserisci Cognome Nome Numero ") + "\n")
        c=input("Vuoi inserire altre persone?(si/no) ").lower()
    fileOut.close()
def caricaPersona(nome):
    fileOut=open(nome, "a")
    fileOut.write(input("Inserisci Cognome Nome Numero" ) + "\n")
    fileOut.close()
def visualizza(nome):
    fileIn= open(nome, "r")
    for line in fileIn:
        print(line)
    fileIn.close()
def ricercaNumero(nome):
    fileIn=open(nome,"r")
    cognome=input("Inserisci cognome per cercare il numero ")
    count=0
    for line in fileIn:
        line=line.rstrip()
        parts=line.split()
        if parts[0]==cognome:
            print("Il cognome è stato trovato ecco i dati")
            print(cognome + " " + parts[2])
            count= count+1
    if count==0:
        print("Cognome non trovato vuoi aggiungere un altro contatto? (si/no)")
        scelta=input().lower()
        if scelta=="si":
            caricaPersona(nome)
        else:
            print("Operazione terminata senza successo ")
    fileIn.close()
def ricercaCognome(nome):
    fileIn=open(nome,"r")
    numero=input("Inserisci il numero per cercare il cognome ")
    count=0
    for line in fileIn:
        line=line.rstrip()
        parts=line.split()
        if parts[2]==numero:
            print("Il numero è stato trovato ecco i dati")
            print(numero + " " + parts[0] + " " + parts[1])
            count= count+1
    if count==0:
        print("Numero non trovato vuoi aggiungere un altro contatto? (si/no)")
        scelta=input().lower()
        if scelta=="si":
            caricaPersona(nome)
        else:
            print("Operazione terminata senza successo ")
    fileIn.close()                   
     
def ricercaNomi(nome):
    fileIn=open(nome,"r")
    n=input("Inserisci il nome del contatto per cercare il cognome e numero ")
    count=0
    for line in fileIn:
        line=line.rstrip()
        parts=line.split()
        if parts[1]==n:
            print("Il nome è stato trovato ecco i dati")
            print(n + " " + parts[0] + " " + parts[2])
            count= count+1
    if count==0:
        print("Nome non trovato vuoi aggiungere un altro contatto? (si/no)")
        scelta=input().lower()
        if scelta=="si":
            caricaPersona(nome)
        else:
            print("Operazione terminata senza successo ")
    fileIn.close()  
def modificaNumero(nome):
    fileIn=open(nome, "r")
    fileOut=open("nuovo.txt", "w")
    content = fileIn.readlines()
    print(content)
    cognome=input("Inserisci il cognome per modificare il suo numero di telefono ")
    i=0
    trovato=0
   
    while i< len(content) and trovato==0:
    
        line=content[i]
        line=line.rstrip()
        parts=line.split()
        
        if parts[0]==cognome:
            numero=input("Inserisci il nuovo numero di " + cognome)
            parts[2]=numero
            trovato=1
        else:
            i=i+1
    if trovato==1:
        content[i]=" ". join(parts) + "\n"
    else:
        print("Elemento non trovato ")
       
    for line in content:
       fileOut.write(line)
    fileOut.flush()
    os.remove(nome)
    os.rename("nuovo.txt", nome)
    fileIn.close()
    fileOut.close()
def modificaNumero1(nome):
    fileIn=open(nome, "r+")
    content = fileIn.readlines()
    print(content)
    cognome=input("Inserisci il cognome per modificare il suo numero di telefono ")
    i=0
    trovato=0
    while i< len(content) and trovato==0:
    
        line=content[i]
        line=line.rstrip()
        parts=line.split()
        
        if parts[0]==cognome:
            numero=input("Inserisci il nuovo numero di " + cognome)
            parts[2]=numero
            trovato=1
            p =" ". join(parts) + "\n"
            content[i]=p
        else:
            i=i+1
    if trovato==1:
        fileIn.close()
        fileOut=open(nome, "w")
        for line in content:
            fileOut.write(line)
        fileOut.close()
    else:
        print("Il cognome non è stato trovato quindi nessuna modifica")
        fileOut.close()

def main():
    nome=input("Inserisci nome del file da aprire ")
    continua="si"
    while continua=="si":
        print("MENU")
        print("1) Caricare una rubrica con molti nomi")
        print("2) cCricare singolo elemento")
        print("3) Visualizzare la rubrica creata")
        print("4) Ricerca numero telefonico tramite cognome ")
        print("5) Ricerca cognome tramite numero telefonico ")
        print("6) Ricerca del cognome e del numero telefonico tramite nome")
        print("7) Modifica del numero telefonico tarmite cognome ")
        scelta=int(input("Inserisci l'operazione che vuoi eseguire "))
        if scelta==1:
            caricaRubrica(nome)
        elif scelta==2:
            caricaPersona(nome)
        elif scelta==3:
            visualizza(nome)
        elif scelta==4:
            ricercaNumero(nome)
        elif scelta==5:
            ricercaCognome(nome)
        elif scelta==6:
            ricercaNomi(nome)
        elif scelta==7:
            modificaNumero1(nome)

        continua = input("vuoi continuare ad effettuare altre operazioni?(si/no)").lower()
main()
        