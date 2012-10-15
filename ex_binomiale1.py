# -*- coding: utf8 -*-

from __future__ import print_function
from scipy import stats

from sage.all import point
from sage.all import show

# Créer la variable aléatoire
X=stats.binom(100,0.7)


# Générer des nombres suivant la loi
print(X.rvs(10))  # Générer 10 nombres

# Trouver des probabilités
print(X.pmf(70))    # P(X=70)
print(X.pmf(65))    # P(X=65)
print(X.pmf(75))    # P(X=75)

# Probabilités cumulées.
print(X.cdf(60))    # P(X<=60)
print(X.cdf(100))    # P(X<=100), doit être 1
print(X.cdf(0))    # P(X<=100), doit être 0 ou à peu près

# Pour tracer :
G=sum( [point((i,X.pmf(i))) for i in range(0,100)]  )
show(G)
