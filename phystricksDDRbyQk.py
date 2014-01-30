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

    A.put_mark(0.2,135,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,225,"\( D\)",automatic_place=(pspict,"corner"))
    M.put_mark(0.2,0,"\( M\)",automatic_place=(pspict,"W"))
    N.put_mark(0.2,90,"\( N\)",automatic_place=(pspict,"S"))
    P.put_mark(0.2,45,"\( P\)",automatic_place=(pspict,"corner"))

    polyg=Polygon(D,N,P,M)
    polyg.parameters.filled()
    polyg.parameters.fill.color="lightgray"

    pspict.DrawGraphs(rect,rect2,polyg,A,B,C,D,N,M,P)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
