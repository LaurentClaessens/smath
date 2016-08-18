# -*- coding: utf8 -*-
from phystricks import *
def RKXHooRkoXOP():
    pspict,fig = SinglePicture("RKXHooRkoXOP")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    E=Point(3,0)
    L=Point(3,2)

    for p in [A,E,L]:
        p.parameters.symbol=""

    trig=Polygon(A,E,L)
    trig.put_mark(0.2,text_list=["\( A\)","\( E\)","\( L\)"],pspict=pspict)
    cm5=Segment(A,L).get_mark(0.2,None,"\SI{5}{\centi\meter}",pspict=pspict)

    rh=RightAngle(trig.edges[0],trig.edges[1],0,1)
    ang=Angle(A,L,E)
    ang.put_mark(0.3,None,"\SI{50}{\degree}",pspict=pspict)

    pspict.DrawGraphs(trig,rh,ang,cm5)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
