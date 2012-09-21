# -*- coding: utf8 -*-

A=[1,3,6,15] 
B=["bonjour","au revoir","salut"] 

A.append(15)
A.append("un mot")      # Un liste peut mélanger des éléments de différents types

print("Quelque informations sur A :")
print(A)
print(A[0])
print(A[2]) # A[2] n'est pas 3 mais 6 !!

B.append("Ceci est le dernier")


print("Quelque informations sur B :")
print(B[1])
print(B[-1])

