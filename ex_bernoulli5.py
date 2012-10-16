from scipy import stats
import math

X=stats.binom(100,1/6)
liste=[]
for i in range(1,21):
    a=X.rvs()
    liste.append(a)
    print("Le schéma",i,"a donné",a,"succès. Maintenant la moyenne est",sum(liste)/len(liste))

