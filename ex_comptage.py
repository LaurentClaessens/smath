# -*- coding: utf8 -*-
n=0
for i in range(0,1001):
    if len(str(i))==3:
        print(i,"oui")
        n=n+1

print("Quantité de nombres à 3 chiffres :",n)
