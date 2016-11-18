# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
from phystricksLectureGraphnrkEEM import fun
from phystricksLectureGraphnrkEEM import f


def KGOAveW():
    pspict,fig = SinglePicture("KGOAveW")

    pspict.dilatation_X(2.5)
    pspict.dilatation_Y(0.7)

    Z=[z.real_part() for z in f.inverse(0)]

    A=Point(Z[0],0)
    B=Point(Z[1],0)
    C=Point(Z[2],0)

    A.put_mark(0.2,text="\( A\)",pspict=pspict,position="N")
    B.put_mark(0.2,text="\( B\)",pspict=pspict,position="N")
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="N")

    g=fun.graph(-0.4,3/2)
    g.wave(0.1,0.05)
    g.parameters.color="red"

    h=phyFunction(2).graph(f.mx,f.Mx)
    h.parameters.color="brown"

    pspict.axes.single_axeX.Dx=0.5
    pspict.DrawGraphs(f,A,B,C,g,h)
    
    pts=Intersection(f,h)
    for i,P in enumerate(pts):
        P.put_mark(0.2,text="\( K_{}\)".format(i+1),pspict=pspict,position="S")
        pspict.DrawGraphs(P)

    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
