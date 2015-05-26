# -*- coding: utf8 -*-
from phystricks import *
def HUGKooTkDsOg():
    pspict,fig = SinglePicture("HUGKooTkDsOg")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(1,2)
    C=B+(4,-4)
    D=A+C-B

    parall=Polygon(A,B,C,D)
    parall.put_mark(0.2,pspict=pspict)

    pspict.DrawGraphs(parall)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
