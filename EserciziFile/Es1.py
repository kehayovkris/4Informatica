"Leggere due file inseriti nel compito(worldpop.txt, worldarea.txt): "
"il primo contiene dati sulla"
"popolazione, nazione per nazione, mentre nel secondo si trovano i dati sulla superficie, in"
"chilometri quadrati; le nazioni sono elencate nello stesso ordine nei du file. Creare una cartella in"
"cui inserite i due file caricati e lo stesso programma che state creando."
"Scrivere il file world_pop_density_txt che contenga i nomi delle nazioni e le relative densità di"
"popolazione(abitanti per km/quadrato), con i nome delle nazioni incolonnati a sinistra e i numeri"
"incolonnati a destra:"



wordarea=open("worldarea.txt","r+")
wordpop=open("worldarea.txt","r+")
word=open("word.txt","r+")

tab=[]

for line in wordpop:
    tab.append(line.split())

for line in wordarea:
    s=line.split()
    p=s.pop(0)
    tab.append(s)

for el in tab:
    word.write("\n")
    for l in el:
        word.write(l + " ")

wordarea.close()
wordpop.close()












