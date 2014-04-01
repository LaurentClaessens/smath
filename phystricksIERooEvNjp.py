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

    A.put_mark(0.2,45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))

    pspict.force_math_bounding_box( C-B+A+(1,1) )

    pspict.DrawGraphs(A,B,C)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
