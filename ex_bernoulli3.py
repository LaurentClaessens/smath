def compte_frequence(A):
    compte=[]
    for i in range(0,max(A)+1):
        compte.append(    len( [x for x in A if x==i] )     )
    return compte
