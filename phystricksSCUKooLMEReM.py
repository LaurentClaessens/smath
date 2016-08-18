# -*- coding: utf8 -*-
from phystricks import *
def SCUKooLMEReM():
    pspict,fig = SinglePicture("SCUKooLMEReM")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,1)
    C=Segment(B,A).rotation(-90).F

    trig=Polygon(A,B,C)
    trig.put_mark(0.4,pspict=pspict)

    rh=RightAngleAOB(C,B,A,n1=0,n2=1)
    trig.edges[0].put_mark(0.2,angle=None,added_angle=180,text="\( 4\)",pspict=pspict)
    trig.edges[2].put_mark(0.2,angle=None,added_angle=180,text="\( ?\)",pspict=pspict)

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
