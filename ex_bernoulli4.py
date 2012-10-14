def sauvegarde(A,nom_de_fichier):
    f=open(nom_de_fichier+".csv","w")
    l=list(A.keys())
    l.sort()
    for i in l:
        f.write(str(i)+","+str(A[i])+"\n")

