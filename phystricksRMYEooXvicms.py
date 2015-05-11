# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def RMYEooXvicms():
    pspict,fig = SinglePicture("RMYEooXvicms")
    pspict.dilatation(0.7)

    h=4
    l=6
    B=Point(0,0)
    A=Point(l/2,h/2)
    C=B+(l,0)
    D=B+C-A

    loz=Polygon(B,A,C,D)
    loz.put_mark(0.2,points_names="BACD",pspict=pspict)

    d1=Segment(A,D)
    d2=Segment(B,C)
    d1.parameters.style="dashed"
    d2.parameters.style="dashed"

    O=Point(A.x,B.y)
    O.put_mark(0.2,angle=90+45,added_angle=0,text="\( O\)",automatic_place=(pspict,""))
    rh=RightAngleAOB(A,O,C)

    no_symbol(loz.vertices)
    pspict.DrawGraphs(loz,d1,d2,O,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
