
#Il punteggio complessivo di una serie di questionari si ottiene sommando tutti i singoli punteggi,
#escludendo i due più bassi. Se, ad esempio, i punteggi nei singoli questionari sono 8,4,7,8.5, 9.5,
#7, 5 e 10, il punteggio complessivo è 50. Scrivere un programma che calcoli il punteggio
#complessivo nel modo appena descritto
from random import random


def generaQuestionario():
    q=[]
    for i in range(0, 5):
        q.append(random.randint(1, 10))
    return q

def calcolaPunteggio(q):
    punteggio=0
    for i in range(2):
        qq=sorted(q)
        r1=qq.pop(0)
        r2=qq.pop(1)
    for i in range(len(qq)):
        punteggio+=qq[i]
    return punteggio

q=generaQuestionario()
print(q)
print(calcolaPunteggio(q))

