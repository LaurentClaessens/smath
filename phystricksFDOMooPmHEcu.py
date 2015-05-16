# -*- coding: utf8 -*-
from phystricks import *
def FDOMooPmHEcu():
    pspict,fig = SinglePicture("FDOMooPmHEcu")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,3)
    C=Point(1,4)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)

    M=trig.edges[0].midpoint()
    trig.edges[0].divide_in_two(n=2,d=0.1,l=0.2,angle=45,pspict=pspict)
    mediane=Segment(  trig.vertices[2],M ).dilatation(1.5)
    mediane.parameters.style="dashed"

    M.put_mark(0.2,angle=None,added_angle=180,text="\( M\)",automatic_place=(pspict,""))

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,mediane,M)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
