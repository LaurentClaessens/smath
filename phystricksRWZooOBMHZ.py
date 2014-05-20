# -*- coding: utf8 -*-
from phystricks import *
def RWZooOBMHZ():
    pspict,fig = SinglePicture("RWZooOBMHZ")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.7)

    mx=-3
    Mx=3

    x=var('x')
    F=[]
    #F.append(phyFunction(1/(x+2)).graph(mx,Mx))
    F.append(phyFunction((0.5*x+1)/(x-1)).graph(mx,Mx))
    F.append(phyFunction((2-x)/(x-1)).graph(mx,Mx))
    F.append(phyFunction(1/x).graph(mx,Mx))

    for f in F:
        f.cut_y(-4,4)

    import random
    random.shuffle(F)

    pspict.DrawGraphs(F)
    #pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
