# -*- coding: utf8 -*-
from phystricks import *
def NARooFiHuAy():
    pspict,fig = SinglePicture("NARooFiHuAy")
    pspict.dilatation_X(0.3)
    pspict.dilatation_Y(0.3)

    A=Point(0,0)
    B=Point(8,0)
    C=Point(8,6)

    triangle=Polygon(A,B,C)
    triangle.edges[0].put_mark(0.2,-90,"\( 8\)",automatic_place=(pspict,"N"))
    triangle.edges[1].put_mark(0.2,0,"\( 6\)",automatic_place=(pspict,"W"))

    A.put_mark(0.2,180+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))

    rh=RightAngle(  triangle.edges[0],triangle.edges[1],0,1)

    pspict.DrawGraphs(triangle,A,B,C,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
