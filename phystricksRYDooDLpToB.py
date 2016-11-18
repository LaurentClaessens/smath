# -*- coding: utf8 -*-
from phystricks import *
def RYDooDLpToB():
    pspict,fig = SinglePicture("RYDooDLpToB")
    pspict.dilatation_X(3)
    pspict.dilatation_Y(3)

    l=3
    h=1

    A=Point(0,0)
    B=A+(l,0)
    C=B+(0,-h)
    D=C+(-l,0)
    rect=Polygon(A,B,C,D)

    P=Segment(C,D).midpoint()
    Q=Segment(A,D).midpoint()

    P.parameters.symbol=""
    Q.parameters.symbol=""

    P.put_mark(0.2,text="\( 15\)",pspict=pspict,position="N")
    Q.put_mark(0.2,text="\(\ell\)",pspict=pspict,position="E")

    pspict.DrawGraphs(rect,P,Q)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
