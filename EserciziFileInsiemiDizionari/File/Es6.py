#A partire dal file numeri.txt costruire un nuovo file numeriPari.txt che contenga solo i numeri
#pari del file numeri e calcolare il valore massimo di tali numeri.



numeri=open("numeri.txt","r")
numeriPari=open("numeriPari.txt","w")



for line in numeri:
    s=line.split()
    l=[]
    for el in s:
        if el.isnumeric():
            n=el
            l.append(n)
            if n%2==0:
                m=max(l)
                numeriPari.write(str(n))

numeri.close()
npr=open("numeriPari.txt","r")
print(npr.read())



