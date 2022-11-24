#Creare un file che contenga 5 numeri interi scritti un per ogni riga nominandolo numeri.txt
import random

numeri=open("numeri.txt","r+")

for i in range(5):
    rn=random.randint(0,100)
    numeri.write(str(rn))

print(numeri.read())
numeri.close()

