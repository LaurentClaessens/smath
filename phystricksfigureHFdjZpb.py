# -*- coding: utf8 -*-
from phystricks import *
def figureHFdjZpb():
    pspict,fig = SinglePicture("figureHFdjZpb")
    pspict.dilatation(1)

    A=Point(-1,1)
    B=Point(2,2)
    D=Point(2,-1)
    C=Point(-1,-1)

    A.put_mark(0.2,90+45,"\( A\)",pspict=pspict)
    B.put_mark(0.2,0,"\( B\)",pspict=pspict)
    C.put_mark(0.2,180+45,"\( C\)",pspict=pspict)
    D.put_mark(0.2,0,"\( D\)",pspict=pspict)

    pspict.DrawGraphs(A,B,C,D)
    pspict.axes.no_numbering()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
