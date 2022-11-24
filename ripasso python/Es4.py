continua = False
n = []
tot = 0

print("Inserisci numeri e Per interromepere digitazione scrivere 0")
while continua == False:
    nc = input()
    if nc == "0":
        continua = True
    else:
        n.append(int(nc))
if len(n) % 2 != 0:
    n.append(0)

for i in range(0, len(n), 2):
    nc = n[i] - n[i + 1]
    tot += n
print(tot)