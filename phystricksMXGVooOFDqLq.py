# -*- coding: utf8 -*-
from phystricks import *
def MXGVooOFDqLq():
    pspict,fig = SinglePicture("MXGVooOFDqLq")
    pspict.dilatation(0.8)

    A=Point(0,0)
    B=Point(3,0)
    C=Point(3,2)

    trig=Polygon(A,B,C)
    rh=RightAngleAOB(A,B,C,n1=0,n2=1)
    angle=Angle(B,A,C)
    angle.put_mark(0.2,angle=None,added_angle=0,text="\( a\)",automatic_place=(pspict,""))

    trig.edges[0].put_mark(0.2,angle=None,added_angle=180,text="\( 5\)",automatic_place=(pspict,""))
    trig.edges[2].put_mark(0.1,angle=None,added_angle=180,text="\( 12\)",automatic_place=(pspict,""))
    trig.put_mark(0.2,pspict=pspict)

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,rh,angle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
