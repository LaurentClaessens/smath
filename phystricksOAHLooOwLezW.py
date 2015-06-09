# -*- coding: utf8 -*-
from phystricks import *
def OAHLooOwLezW():
    pspict,fig = SinglePicture("OAHLooOwLezW")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(0.5)

    l=4
    A=Point(0,0)
    B=Point(l,0)
    C=Point(l,l)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)
    trig.edges[0].put_code(n=2,d=0.1,l=0.2,pspict=pspict)
    trig.edges[1].put_code(n=2,d=0.1,l=0.2,pspict=pspict)

    no_symbol(trig.vertices)
    pspict.DrawGraphs(trig)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

