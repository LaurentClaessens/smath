# -*- coding: utf8 -*-
from phystricks import *
def VectoMilieuNuWgHW():
    pspict,fig = SinglePicture("VectoMilieuNuWgHW")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,2)
    M=Segment(A,B).center()

    A.put_mark(0.2,-45,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,-45,"\( B\)",automatic_place=pspict)
    M.put_mark(0.2,-45,"\( M\)",automatic_place=pspict)

    AM=AffineVector(A,M)
    MB=AffineVector(M,B)
    AM.parameters.color="blue"
    MB.parameters.color="green"

    pspict.DrawGraphs(A,B,M,AM,MB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
