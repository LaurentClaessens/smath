import random
import math

def lancer():
    x=random.randint(1,6)
    if x == 5 or x == 6 :
        return 1
    else :
        return 0

def jeu():
    gain=0
    for i in range(0,200):
        a=lancer()
        if a==1 :
            gain=gain+1
    return gain

def plusieurs_jeux():
    A=[]
    for i in range(0,500):
        A.append(  jeu()   )
    return A

def graphique():
    import matplotlib
    import matplotlib.pyplot
    matplotlib.use('Agg') 
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(111)

    A=plusieurs_jeux()
    X=[]
    Y=[]
    for i,f in enumerate(  A  ):
        X.append(i)
        Y.append(f)
    ax.scatter(X,Y)

    fig.savefig('mon_beau_graphique.png')

graphique()
