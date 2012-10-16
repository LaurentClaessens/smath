# -*- coding: utf8 -*-

from scipy import stats

# Créer la variable aléatoire
X=stats.binom(100,0.7)

# Générer des nombres suivant la loi
print("Dix tirages aux hasard : ",X.rvs(10))  # Générer 10 nombres

# Trouver des probabilités
print("P(X=70)",X.pmf(70))    # P(X=70)
print("P(X=65)",X.pmf(65))    # P(X=65)
print("P(X=75)",X.pmf(75))    # P(X=75)

# Probabilités cumulées.
print("P(X<60)",X.cdf(60))    # P(X<=60)
print("P(X<=100)",X.cdf(100))    # P(X<=100), doit être 1
print("P(X<=0)",X.cdf(0))    # P(X<=100), doit être 0 ou à peu près

