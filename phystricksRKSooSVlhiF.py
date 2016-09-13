# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def RKSooSVlhiF():
    pspict,fig = SinglePicture("RKSooSVlhiF")
    pspict.dilatation_X(0.3)
    pspict.dilatation_Y(0.3)

    l=10
    x=3
    A=Point(0,0)
    B=Point(l,0)
    M=Segment(A,B).midpoint()
    C1=Point(x/2,0)
    C2=Point( x+(l-x)/2,0  )
    I=Point(x,0)
    grand_cercle=Circle(M,l/2).graph(0,180)
    cer1=Circle( C1,x/2 ).graph(0,180)
    cer2=Circle( C2,  (l-x)/2 ).graph(0,180)

    grand_cercle.parameters.filled()
    grand_cercle.parameters.fill.color="lightgray"
    cer1.parameters.filled()
    cer1.parameters.fill.color="white"
    cer2.parameters.filled()
    cer2.parameters.fill.color="white"

    I.put_mark(0.2,-45,"\( I\)",pspict=pspict,position="corner")
    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-90,"\( B\)",pspict=pspict,position="N")

    for P in [I,A,B]:
        P.parameters.symbol=""

    measureAI=MeasureLength(  Segment(A,I) ,0.3  )
    measureAI.put_mark(0.3,-90,"\( x\)",pspict=pspict,position="N")

    pspict.DrawGraphs(grand_cercle,cer1,cer2,A,B,I,measureAI)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
