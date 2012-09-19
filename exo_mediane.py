>>> l=[10,13,0,2,18,10,16,9,0,9,9,5,5,6,5,8,12,12,8,11,11,2,8,17,10,10,14]
>>> len(l)
27              # La liste contient 27 valeurs
>>> l.sort()    # Pour trier la liste
>>> l
[0, 0, 2, 2, 5, 5, 5, 6, 8, 8, 8, 9, 9, 9, 10,
        10, 10, 10, 11, 11, 12, 12, 13, 14, 16, 17, 18]
>>> sum(l)
240             # La somme des nombres de la liste

# Pour le premier quartile

>>> len(l)/4
6.75            # Il faut prendre la septième valeur.
>>> l[6]        # !!!! La septième valeur est l[6] et non l[7]
                # parce que la première valeur est l[0] et non l[1].
5  

# Pour le second quartile

>>> 3*len(l)/4
20.25
>>> l[20]
12

# Pour la médiane

>>> 27/2
13.5        # Il faut prendre la douzième valeur
>>> l[11]   # Et non l[12]
9
