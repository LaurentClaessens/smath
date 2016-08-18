# -*- coding: utf8 -*-
from phystricks import *
def HMUTooSSSCZl():
    pspict,fig = SinglePicture("HMUTooSSSCZl")
    pspict.dilatation(1.2)

    A=Point(0,0)
    B=Point(0,2)
    C=Point(2,2)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)
    rh=RightAngleAOB(C,B,A)

    ang=AngleAOB(C,A,B) 
    ang.put_mark(0.2,angle=None,added_angle=0,text="\SI{40}{\degree}",pspict=pspict)

    trig.edges[1].put_mark(0.2,angle=None,added_angle=0,text="\SI{6}{\centi\meter}",pspict=pspict)

    no_symbol(trig.vertices)
    pspict.DrawGraphs(trig,rh,ang)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
