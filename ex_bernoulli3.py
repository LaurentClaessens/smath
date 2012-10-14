def compte_frequence(A):
    d={}
    for i in range(0,101):
        d[i]=A.count(i)
    return d
