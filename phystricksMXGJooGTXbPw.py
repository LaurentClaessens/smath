# -*- coding: utf8 -*-
from phystricks import *
def MXGJooGTXbPw():
    pspict,fig = SinglePicture("MXGJooGTXbPw")
    pspict.dilatation(1.5)

    A=Point(0,0)
    B=Point(0.3,4)
    C=Segment(B,A).rotation(-90).dilatation(2).F

    trig=Polygon(A,B,C)
    trig.put_mark(0.3,pspict=pspict)

    rh=RightAngleAOB(C,B,A,r=0.7)
    ang=AngleAOB(B,A,C)
    ang.put_mark(text="\SI{30}{\degree}",pspict=pspict)

    trig.edges[1].put_measure(measure_distance=0.5,mark_distance=-0.3,mark_angle=None,text="\SI{3}{\centi\meter}",pspict=pspict)

    no_symbol(trig.vertices)
    pspict.DrawGraphs(trig,rh,ang)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
