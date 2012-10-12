texte="rarissime"
liste=[]
for a in texte.split("r")[1:]:
    liste.append("r"+a[0])

print(liste)

