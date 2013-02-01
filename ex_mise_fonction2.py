import random
import re

texte_reference="Ceci devrait être un assez long texte"

def lettre_suivante(k):
    resultats=re.compile(k+".").findall(texte_reference)   
    a=random.choice(resultats)           
    return a[-1]

s=lettre_suivante("e")
print(s)
