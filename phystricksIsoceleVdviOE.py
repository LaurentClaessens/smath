# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def IsoceleVdviOE():
    pspict,fig = SinglePicture("IsoceleVdviOE")
    pspict.dilatation(0.7)

    l=5

    A=Point(0,0)
    B=Point(l,0)

    C1=Circle(A,2*l/3).graph(-90,90)
    C2=Circle(B,2*l/3).graph(90,270)

    pts=Intersection(C1,C2)
    I=pts[0]
    J=pts[1]

    seg=Segment(A,B).dilatation(1.3)
    IJ=Segment(I,J).dilatation(1.3)
    IJ.parameters.color="red"
    M=Intersection(IJ,seg)[0]

    I.put_mark(0.2,0,"\( I\)",automatic_place=pspict)
    J.put_mark(0.2,0,"\( J\)",automatic_place=pspict)
    A.put_mark(0.2,90,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,90,"\( B\)",automatic_place=pspict)
    M.put_mark(0.2,45,"\( M\)",automatic_place=pspict)

    C1.parameters.style="dashed"
    C1.parameters.color="blue"
    C2.parameters.style="dashed"
    C2.parameters.color="blue"


    pspict.DrawGraphs(A,B,C1,C2,seg,IJ,I,J,M)
    #pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

