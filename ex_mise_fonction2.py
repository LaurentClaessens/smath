texte="rarissime"

def paires(k):
    liste=[]
    for a in texte.split(k)[1:]:
        liste.append(k+a[0])
    return liste

print(paires("r"))
