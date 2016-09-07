# -*- coding: utf8 -*-
from phystricks import *
def KYbSnVB():
    pspict,fig = SinglePicture("KYbSnVB")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    A=Point(2,3)
    B=Point(5,5)
    C=Point(1,1)
    D=Point(-2,-1)

    A.put_mark(0.2,135,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict,position="corner")
    D.put_mark(0.2,225,"\( D\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(A,B,C,D)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
