from time import * 
from datetime import *
def horloge():
    while True:
        print(str(datetime.now())[11:19])
        sleep(1)





heure_alarme = input("Entrez l'heure de l'alarme (HH:MM:SS): ")

def afficher_heure(h, m, s):
    l = [0,1,2,3,4,5,6,7,8,9]
    print(datetime.now())
    while True:
        s = s+1
        if s == 60:
            m += 1 
            s = 0
        if m == 60:
            h += 1
            m = 0
            s = 0
        if h == 24:
            h = 0
        if h in l or m in l or s in l:
            H = str(h)
            M = str(m)
            S = str(s)
            if h in l:
                H = "0" + H
            if m in l:
                M = "0" + M 
            if s in l:
                S = "0" + S 
            print(H + ":" + M + ":" + S)
        else:
            print(str(h)+":"+ str(m)+":"+str(s))
        
        if H + ":" + M + ":" + S == heure_alarme:
            print("Alarme!")
        sleep(1)
afficher_heure(12,00,00),horloge()