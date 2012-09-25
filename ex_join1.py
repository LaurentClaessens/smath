texte="Voici mon texte"
l=list(texte)

# Notez la différence entre les deux choses affichées :
print(texte)
print(l)

# Conversion inverse

A=["un","deux","trois zéro"]
texte=" et ".join(A)
print(A)
print(texte)
# Notez que python n'ajoute " et " que ENTRE les éléments de la liste, pas avant.
