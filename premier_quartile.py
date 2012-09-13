import math                     # On importe les fonctions mathématiques de base

def premier_quartile(liste):
    liste.sort()             # 'to sort' : trier an anglais
    n=len(liste)            # 'len' donne la longueur de la liste
    a=n/4
    numero=math.ceil(a)     # 'ceiling' signigie "plafond" en anglais
                            # math.ceil(a) est le nombre entier
                            # arrondi au plus grand à partir de a.

    return liste[numero-1]  # en python, les listes sont numérotées 
                            #à partir de 0 et non de 1.


Q1=premier_quartile([1,5,2,4,3,8,6,7,9])
print(Q1)
