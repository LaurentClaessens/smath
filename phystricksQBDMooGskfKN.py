# -*- coding: utf8 -*-
from phystricks import *

def QBDMooGskfKN():
    pspict,fig = SinglePicture("QBDMooGskfKN")
    pspict.dilatation(0.7)

    A=Point(3,2)
    B=Point(-5,3)
    C=Point(1,-4)
    H=Point(-3.5,0)

    A.put_mark(0.2,45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,90+45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict,position="corner")
    H.put_mark(0.2,text="\( H\)",pspict=pspict,position="S")

    for P in [A,B,C]:
        qx=Point(P.x,0)
        qy=Point(0,P.y)
        s1=Segment(P,qx)
        s2=Segment(P,qy)
        s1.parameters.style="dashed"
        s2.parameters.style="dashed"
        pspict.DrawGraphs(s1,s2)

    pspict.DrawGraphs(A,B,C,H)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
