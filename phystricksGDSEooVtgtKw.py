# -*- coding: utf8 -*-
from phystricks import *
def GDSEooVtgtKw():
    pspict,fig = SinglePicture("GDSEooVtgtKw")
    pspict.dilatation(0.6)

    A=Point(3,2)
    B=Point(-3,4)
    C=Point(0,-4)
    H=Point(-6.5,-2)

    A.put_mark(0.2,A.angle(),"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,B.angle(),"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))
    H.put_mark(0.2,H.angle(),"\( H\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(A,B,C,H)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
