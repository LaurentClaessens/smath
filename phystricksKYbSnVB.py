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

    A.put_mark(0.2,135,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,225,"\( D\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(A,B,C,D)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
