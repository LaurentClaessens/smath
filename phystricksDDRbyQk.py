# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def DDRbyQk():
    pspict,fig = SinglePicture("DDRbyQk")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=6
    h=4

    k=h/3

    D=Point(0,0)
    C=D+(l,0)
    B=C+(0,h)
    A=B-(l,0)

    N=A+(k,0)
    M=C+(0,k)
    P=Point(N.x,M.y)

    rect2=Polygon(N,P,M,B)
    rect=Polygon(A,B,C,D)

    A.put_mark(0.2,135,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict,position="corner")
    D.put_mark(0.2,225,"\( D\)",pspict=pspict,position="corner")
    M.put_mark(0.2,text="\( M\)",pspict=pspict,position="W")
    N.put_mark(0.2,text="\( N\)",pspict=pspict,position="S")
    P.put_mark(0.2,45,"\( P\)",pspict=pspict,position="corner")

    polyg=Polygon(D,N,P,M)
    polyg.parameters.filled()
    polyg.parameters.fill.color="lightgray"

    pspict.DrawGraphs(rect,rect2,polyg,A,B,C,D,N,M,P)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
