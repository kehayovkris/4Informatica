class NoleggioAuto:
    "Nel costruttore ho messo come noleggio standard 5 giorni"
    def __init__(self):
        self.__nome=""
        self.__giorni=5
        self.__tariffa="standard"



    def calcolaprezzo(self):
        if self.__giorni>=20:
            self.__tariffa="special"
            self.__prezzo=self.__giorni*85 + int(input("inserire kilometri aggiuntivi"))*0.24
        else:
            self.__prezzo = self.__giorni * 85

    def setnome(self,n):
        self.__nome=n

    def getnome(self):
        return self.__nome

    def getgiorni(self):
        return self.__giorni
    def gettariffa(self):
        return self.__tariffa

    def getprezzo(self):
        return self.__prezzo

    def setgiorni(self,g):
        self.__giorni=g

    def settariffa(self, t):
        self.__tariffa = t

    def setprezzo(self,p):
        self.__prezzo=p

    def __str__(self):
        print("Il numeoro dei giorni è"+str(self.__giorni)+"La tariffa finale è"+str(self.__tariffa))


