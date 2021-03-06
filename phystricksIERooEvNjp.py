# -*- coding: utf8 -*-
from phystricks import *
def IERooEvNjp():
    pspict,fig = SinglePicture("IERooEvNjp")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    A=Point(2,2)
    B=Point(0,0)
    C=Point(3,0)

    A.put_mark(0.2,45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,45,"\( C\)",pspict=pspict,position="corner")

    pspict.force_math_bounding_box( C-B+A+(1,1) )

    pspict.DrawGraphs(A,B,C)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
