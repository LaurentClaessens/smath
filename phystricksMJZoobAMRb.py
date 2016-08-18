# -*- coding: utf8 -*-
from phystricks import *
def MJZoobAMRb():
    pspict,fig = SinglePicture("MJZoobAMRb")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(1,1)
    B=Point(-3,3)
    C=Point(3,1)

    A.put_mark(0.2,-45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,90+45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(A,B,C)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
