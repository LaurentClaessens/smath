# -*- coding: utf8 -*-
from phystricks import *
def MAXkaGz():
    pspict,fig = SinglePicture("MAXkaGz")
    pspict.dilatation_X(0.47)
    pspict.dilatation_Y(0.3)

    eff={}

    import string
    for c in string.ascii_lowercase:
        eff[c]=0

    eff['a']=4
    eff['b']=8
    eff['c']=9
    eff['d']=2
    eff['h']=2
    eff['j']=1
    eff['l']=1
    eff['m']=2
    eff['p']=2
    eff['r']=1
    eff['s']=1
    eff['t']=2

    cum=0
    for i,c in enumerate(string.ascii_lowercase):
        cum=cum+eff[c]
        P=Point(i+1,cum)
        Q=Point(i+1,0)
        Q.put_mark(0.2,-90,c,automatic_place=(pspict,"N"))
        Q.parameters.symbol="none"
        pspict.DrawGraphs(P,Q)



    pspict.axes.single_axeX.no_numbering()
    pspict.axes.single_axeY.Dx=2
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
