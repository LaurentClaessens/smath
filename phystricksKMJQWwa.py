# -*- coding: utf8 -*-
from phystricks import *

x=var('x')

def grille(fun=None):
    l=[]
    for x in range(1,11):
        for y in range(1,11):
            P=Point(x,y)
            P.parameters.symbol="x"
            if fun:
                if fun(P.x)==P.y:
                    P.parameters.symbol="*"
                    P.parameters.color="blue"
            l.append(P)
    return l

def KMJQWwa():
    pspicts,fig = MultiplePictures("KMJQWwa",3)
    pspicts[0].mother.caption=""
    pspicts[1].mother.caption=""
    pspicts[2].mother.caption=""

    for psp in pspicts:
        psp.dilatation_X(0.7)
        psp.dilatation_Y(0.7)
    pspicts[0].DrawGraphs(grille())

    s1=phyFunction(x+5).graph(0,6)
    pspicts[1].DrawGraphs(s1)
    pspicts[1].DrawGraphs(grille(s1))

    s2=phyFunction(2*x).graph(0,5.5)
    Q=Point(1,2)
    pspicts[2].DrawGraphs(grille(s2))
    Q.parameters.color="red"
    pspicts[2].DrawGraphs(s2,Q)


    for psp in pspicts:
        psp.axes.do_mx_enlarge=False
        psp.axes.do_my_enlarge=False
        #psp.DrawDefaultGrid()
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
