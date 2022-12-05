from NoleggioAuto import *
class NoleggioCamper(NoleggioAuto):

    def __init__(self):
        super(NoleggioCamper, self).__init__()


    def calcolaprezzo(self):
        if self.getgiorni() >= 20:
            self.settariffa("Special")
            self.setprezzo(int(self.getgiorni())*65+int(input("inserire kilometri aggiuntivi")) * 0.24 + 200)
        else:
            self.setprezzo(int(self.getgiorni())*65+200)






