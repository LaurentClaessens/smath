print("Bonjour !")

liste=[]                # liste vide
liste.extend(3*[40])    # 3*[40] est la liste [40,40,40]
liste.extend(5*[41])
liste.extend(10*[42])
liste.extend(8*[43])
liste.extend(2*[44])
liste.extend(4*[45])

print(liste)           # Afficher liste
        
#   [40,40,40,41,41,41,41,41,42,42,42,42,42,42,42,42,42,42,43,
#   43,43,43,43,43,43,43,44,44,45,45,45,45]

n=len(liste)        # len(liste) est la longueur de la liste
somme=sum(liste)    # la somme de la liste

print(n)        # 32      
print(somme)    # 1357

moyenne=somme/n     # diviser la somme la la longueur donne la moyenne

print(moyenne)  # 42.40625
