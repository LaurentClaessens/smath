import math                     # On importe les fonctions mathématiques de base

def mediane(liste):
    liste.sort()             # 'to sort' : trier an anglais
    n=len(liste)            # 'len' donne la longueur de la liste

    if n%2 == 0:        # teste si n est pair
        numero=int(n/2)
        Me = (liste[numero-1]+liste[numero])/2
        return Me
    else :
        numero=math.ceil(n/2)
        Me=liste[numero-1]
        return Me


M=mediane([1,2,3,4])
print(M)                    # 2.5
M= mediane([1,2,3,4,5])
print(M)                    # 3
