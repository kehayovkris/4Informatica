class Carta:

    colore=["blu","rosso","verde","giallo"]
    rango=["1","2","3","4","5","7","block","+2","reverse",]

    def __init__(self,c,r):
        self.__color=self.colore[c]
        self.__rango=self.rango[r]


    def getcolor(self, ):
        return self.__color

    def getrango(self,):
        return self.__rango

    def getinfo(self):
        return self.__color+self.__rango



