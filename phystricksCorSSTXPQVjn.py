# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def CorSSTXPQVjn():
    pspict,fig = SinglePicture("CorSSTXPQVjn")
    pspict.dilatation(1)

    l=3
    B=Point(0,0)
    C=Point(l,0)
    A=Point(l*cos(pi/3),l*sin(pi/3))
    A.put_mark(0.2,90,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,180,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,0,"\( C\)",automatic_place=pspict)

    H=A.projection(Segment(B,C))
    H.put_mark(0.2,45,"\( H\)",automatic_place=pspict)

    hauteur=Segment(A,H)
    hauteur.parameters.style='dashed'
    hauteur.parameters.color='blue'

    BC=Segment(B,C)
    measureBC=MeasureLength(BC,0.2)
    measureBC.put_mark(0.3,-90,"\( x\)",automatic_place=pspict)

    triangle=Polygon(A,B,C)
    triangle.parameters.filled()

    pspict.DrawGraphs(triangle,hauteur,A,B,C,H,measureBC)
    fig.conclude()
    fig.write_the_file()

