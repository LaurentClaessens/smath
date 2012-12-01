# -*- coding: utf8 -*-
from phystricks import *
def figureVNaHvXi():
    pspict,fig = SinglePicture("figureVNaHvXi")
    pspict.dilatation(1)

    A=Point(4,3)
    B=Point(0,0)
    C=Point(3,-1)

    trig=Polygon(A,B,C)
    I=Segment(A,B).center()
    J=Segment(A,C).center()

    IJ=Segment(I,J)

    A.put_mark(0.2,90,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,180,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,0,"\( C\)",automatic_place=pspict)
    I.put_mark(0.2,135,"\( I\)",automatic_place=pspict)
    J.put_mark(0.2,0,"\( J\)",automatic_place=pspict)


    pspict.DrawGraphs(trig,IJ,A,B,C,I,J)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

