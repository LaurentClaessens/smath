# -*- coding: utf8 -*-
from phystricks import *
def JOKJMTD():
    pspict,fig = SinglePicture("JOKJMTD")
    pspict.dilatation(0.2)

    h=10
    r=3
    O=Point(0,0)
    A=Point(-r,h)
    B=Point(r,h)

    AB=Segment(A,B)
    S=AB.center()
    cer=Circle(S,r).graph(0,180)

    OA=Segment(O,A)
    OB=Segment(O,B)

    O.put_mark(0.2,0,"\( O\)",pspict=pspict)
    A.put_mark(0.2,-180,"\( A\)",pspict=pspict)
    B.put_mark(0.2,0,"\( B\)",pspict=pspict)

    pspict.DrawGraphs(O,A,B,cer,AB,OA,OB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
