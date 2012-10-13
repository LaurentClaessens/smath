def sauvegarde(A,nom_de_fichier):
    f=open(nom_de_fichier+".csv","w")
    for x in A:
        f.write(str(x)+"\n")

