import random

def bernoulli():
    x=random.uniform(0,1)   # Choisir un nombre au hasard dans l'intervalle [0;1]
    if x<=0.8:
        return 1
    else:
        return 0

a=bernoulli()
print(a)
