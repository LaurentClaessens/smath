# -*- coding: utf8 -*-
from phystricks import *
def GDSEooVtgtKw():
    pspict,fig = SinglePicture("GDSEooVtgtKw")
    pspict.dilatation(0.6)

    A=Point(3,2)
    B=Point(-3,4)
    C=Point(0,-4)
    H=Point(-6.5,-2)

    A.put_mark(0.2,A.angle(),"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,B.angle(),"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,45,"\( C\)",pspict=pspict,position="corner")
    H.put_mark(0.2,H.angle(),"\( H\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(A,B,C,H)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
