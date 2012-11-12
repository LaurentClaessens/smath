# -*- coding: utf8 -*-
from phystricks import *
def figureERITfSy():
    pspict,fig = SinglePicture("figureERITfSy")
    pspict.dilatation(1)

    l=4
    x=2.5
    A=Point(0,0)
    B=Point(0,-x)
    C=Point(l,-x)
    D=Point(l,0)

    A.put_mark(0.2,90,"\( A\)",automatic_place=pspict)
    D.put_mark(0.2,90,"\( D\)",automatic_place=pspict)
    B.put_mark(0.2,225,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,-45,"\( C\)",automatic_place=pspict)

    K=Segment(A,B).center()
    K.put_mark(0.2,180,"\( x\)",automatic_place=pspict)
    K.parameters.symbol="none"

    plage=Segment(A,D).dilatation(1.5)
    ligne=Polygon(A,B,C,D)
    ligne.edge.parameters.color="red"

    plage.parameters.color="blue"

    pspict.DrawGraphs(ligne,plage,K,A,B,C,D)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
