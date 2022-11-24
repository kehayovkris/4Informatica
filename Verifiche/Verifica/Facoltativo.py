def punti():
    s=open("facoltativo.txt","r")
    virgole=0
    punti=0
    for line in s:
        if "," in line:
           virgole+=1
        elif "." in line:
            punti+=1
    print("i punti sono"+str(punti)+"le virgole sono"+str(virgole))
    s.close()

def eliminaspazio():
    s = open("facoltativo.txt", "r")
    for line in s:
       line.rstrip()
    s.close()

def eliminaPunteggiaturaFinale():
    s = open("facoltativo.txt", "r")
    n=open("newFacoltativo.txt","w")
    for line in s:
        if line[len(line)]== "," or "." or "!":
            line.rstrip()
            n.write(line)
    s.close()

punti()
eliminaspazio()
eliminaPunteggiaturaFinale()