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
    angle=AngleAOB(B,A,C)
    angle.put_mark(text="\( a\)",pspict=pspict)

    trig.edges[0].put_mark(added_angle=180,text="\( 5\)",pspict=pspict)
    trig.edges[2].put_mark(added_angle=180,text="\( 12\)",pspict=pspict)
    trig.put_mark(0.2,pspict=pspict)

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,rh,angle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
