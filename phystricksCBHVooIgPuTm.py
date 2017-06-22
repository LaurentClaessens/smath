# -*- coding: utf8 -*-
from phystricks import *
def CBHVooIgPuTm():
    pspict,fig = SinglePicture("CBHVooIgPuTm")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(0.3)

    D=Point(0,0)
    A=D+(0,3)
    B=A+(8,0)
    C=D+B-A

    rect=Polygon(A,B,C,D)
    rect.put_mark(0.2,pspict=pspict)
    rect.filled()
    rect.fill_parameters.color="lightgray"

    H=rect.edges[2].midpoint()
    cer=CircleOA(  H,rect.edges[0].midpoint() ).graph(0,180)
    cer.parameters.filled()
    cer.parameters.fill.color="white"

    no_symbol(rect.vertices)
    pspict.DrawGraphs(rect,cer)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
