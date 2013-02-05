import random

def lancer():
    x=random.randint(1,6)
    if x == 5 or x == 6 :
        return 1
    else :
        return 0

def jeu():
    gain=0
    for i in range(0,100):
        a=tirage()
        if a==1 :
            gain=gain+1
    return n_succes

def plusieurs_jeux():
    A=[]
    for i in range(0,1000):
        A.append(  jeu()   )
    return A
