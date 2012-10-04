# -*- coding: utf8 -*-
from phystricks import *
def ExGrapheOcxXii():
    x=var('x')
    f=phyFunction(2*x+1)

    pspicts,fig = MultiplePictures("ExFonction",2,script_filename="ExGrapheOcxXii")
    pspicts[0].mother.caption="Quelque points du graphe de $f(x)=2x+1$"
    pspicts[1].mother.caption="Le graphe de $f(x)=2x+1$"


    for psp in pspicts:
        psp.dilatation_Y(1)
        psp.dilatation_X(1)

    X=[-2,-1,0,1,1.5]
    
    pspicts[1].DrawGraphs(f.graph(min(X)-0.5,max(X)+0.5))

    for x in X:
        P=Point(x,f(x))
        pspicts[0].DrawGraphs(P)
        pspicts[1].DrawGraphs(P)

    for psp in pspicts:
        psp.DrawDefaultAxes()
        psp.DrawDefaultGrid()

    fig.conclude()
    fig.write_the_file()
