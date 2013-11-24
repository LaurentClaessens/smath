# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def ITzxISE():
    pspict,fig = SinglePicture("ITzxISE")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    A=Point(1,3)
    B=Point(4,1)
    C=Point(9/2,5)

    AB=Segment(A,B)
    M=AB.center()
    AC=Segment(A,C)
    BC=Segment(B,C)
    MC=Segment(M,C)

    A.put_mark(0.2,90,"\( A\)",automatic_place=(pspict,"S"))
    B.put_mark(0.2,0,"\( B\)",automatic_place=(pspict,"W"))
    C.put_mark(0.2,90,"\( C\)",automatic_place=(pspict,"S"))
    M.put_mark(0.2,-90,"\( M\)",automatic_place=(pspict,"N"))

    pspict.DrawGraphs(MC,AB,AC,BC,A,B,C,M)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
