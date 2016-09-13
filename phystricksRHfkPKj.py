# -*- coding: utf8 -*-
from phystricks import *
def RHfkPKj():
    pspict,fig = SinglePicture("RHfkPKj")
    pspict.dilatation_X(3)
    pspict.dilatation_Y(3)

    A=Point(0,0)
    E=Point(0,1)
    F=Point(1,1)
    B=Point(1,0)

    I=Segment(E,F).midpoint()
    J=Segment(B,F).midpoint()
    carre=Polygon(A,E,F,B)

    seg=Segment(I,J)

    A.put_mark(0.2,225,"\( A\)",pspict=pspict,position="corner")
    E.put_mark(0.2,135,"\( E\)",pspict=pspict,position="corner")
    F.put_mark(0.2,45,"\( F\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")
    I.put_mark(0.2,90,"\( I\)",pspict=pspict,position="S")
    J.put_mark(0.2,0,"\( J\)",pspict=pspict,position="W")

    pspict.DrawGraphs(carre,I,J,seg,A,E,F,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

