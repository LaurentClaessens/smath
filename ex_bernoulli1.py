import random

def bernoulli(p):
    x=random.uniform(0,1)   # Choisir un nombre au hasard dans l'intervalle [0;1]
    if x<=p:
        return 1
    if x>p:
        return 0

for i in range(1,100):
    print(bernoulli(0.7))
