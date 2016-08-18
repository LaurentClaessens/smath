# -*- coding: utf8 -*-
from phystricks import *

def GUEjmmR():
    pspict,fig = SinglePicture("GUEjmmR")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    c=3
    A=Point(0,0)
    B=Point(c,0)
    C=Point(c,c)
    D=Point(0,c)

    carre=Polygon(A,B,C,D)
    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,45,"\( C\)",pspict=pspict,position="corner")
    D.put_mark(0.2,90+45,"\( D\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(carre,A,B,C,D)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
