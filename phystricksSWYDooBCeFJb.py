# -*- coding: utf8 -*-
from phystricks import *
def SWYDooBCeFJb():
    pspict,fig = SinglePicture("SWYDooBCeFJb")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    C=Point(0,0)
    B=Point(4,0)
    A=Point(B.x,2)

    trig=Polygon(A,B,C)
    trig.edges[0].put_mark(0.2,angle=None,added_angle=0,text="\( 13\)",automatic_place=(pspict,""))
    trig.edges[1].put_mark(0.2,angle=None,added_angle=0,text="\( 84\)",automatic_place=(pspict,""))
    trig.edges[2].put_mark(0.2,angle=None,added_angle=0,text="\( 85\)",automatic_place=(pspict,""))

    pspict.DrawGraphs(trig)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
