# -*- coding: utf8 -*-
from phystricks import *
def KBOKooTCswpl():
    pspict,fig = SinglePicture("KBOKooTCswpl")
    pspict.dilatation(0.6)

    A=Point(3,2)
    B=Point(-1,4)
    C=Point(0,-1)
    D=Point(-3,-2)

    A.put_mark(0.2,angle=None,text="\( A\)",automatic_place=(pspict,""))
    B.put_mark(0.2,angle=None,text="\( B\)",automatic_place=(pspict,""))
    C.put_mark(0.2,angle=None,text="\( C\)",automatic_place=(pspict,""))
    D.put_mark(0.2,angle=None,text="\( D\)",automatic_place=(pspict,""))

    pspict.math_BB.append( Point(4,4),pspict=pspict )
    pspict.math_BB.append( Point(-4,-4),pspict=pspict )

    pspict.DrawGraphs(A,B,C,D)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
