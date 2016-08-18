# -*- coding: utf8 -*-
from phystricks import *
def WHWXooTAHTOd():
    pspict,fig = SinglePicture("WHWXooTAHTOd")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(0.7)

    A=Point(0,0)
    B=Point(4,0)
    C=B+(0,2)
    D=A+C-B
    rect=Polygon(A,B,C,D)
    O=rect.edges[2].midpoint()
    cer=CircleOA(O,C).graph(0,180)

    rect.parameters.hatched()
    rect.parameters.hatch.color="lightgray"
    cer.parameters.hatched()
    cer.parameters.hatch.color="lightgray"

    #rect.put_mark(0.2,pspict=pspict)
    #O.put_mark(0.2,angle=None,added_angle=0,text="\( O\)",pspict=pspict)

    no_symbol(rect.vertices)
    pspict.DrawGraphs(rect,cer)

    pspict.grid.main_horizontal.parameters.style="dashed"
    pspict.grid.main_vertical.parameters.style="dashed"
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
