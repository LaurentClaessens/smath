# -*- coding: utf8 -*-
from phystricks import *
def OZfyDkr():
    pspict,fig = SinglePicture("OZfyDkr")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    B=Point(0,0)
    C=Point(4,0)
    A=Point(3,2)
    triangle=Polygon(A,B,C)

    A.put_mark(0.2,90,"\( A\)",automatic_place=(pspict,"S"))
    B.put_mark(0.2,180,"\( B\)",automatic_place=(pspict,"E"))
    C.put_mark(0.2,0,"\( C\)",automatic_place=(pspict,"W"))

    pspict.DrawGraphs(A,B,C,triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

