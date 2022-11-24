#Costruire una classe che rappresenti calcolatrice che dati due numeri sia in grado di elaborare
# le quattro operazioni elementari: addizione, sottrazione, moltiplicazione e divisione.
# Creare un metodo main che istanzi la classe calcolatrice,
# fornendo un menù per la scelta delle operazioni
class Calcolatrice:
    x=0
    y=0

    def __init__(self):
        self.x=int(input("Inserisci primo valore"))
        self.y= int(input("Inserisci secondo valore"))

    def addizione(self):
        return self.x+self.y
    def sottrazione(self):
        return self.x - self.y
    def moltiplicazione(self):
        return self.x * self.y
    def divisione(self):
        return self.x/self.y

c=Calcolatrice()
print(c.addizione())
print(c.sottrazione())
print(c.moltiplicazione())
print(c.divisione())