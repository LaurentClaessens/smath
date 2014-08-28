import random

from ex_bernoulli3 import compte_frequence
from ex_bernoulli4 import sauvegarde

def bernoulli(p):
    x=random.uniform(0,1)   # Choisir un nombre au hasard dans l'intervalle [0;1]
    if x<=p:
        return 1
    else:
        return 0

def schema(p,n):
    liste_resultats=[]
    for i in range(0,n):
        a=bernoulli(p)
        liste_resultats.append( a )
    return sum(liste_resultats)

A=[]
for j in range(1,10000):
   A.append(schema(0.8,100))

compte=compte_frequence(A)
print(compte)
sauvegarde(compte,"mon_fichier")
