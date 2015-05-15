# -*- coding: utf8 -*-
from phystricks import *
def XUATooMWfESC():
    pspict,fig = SinglePicture("XUATooMWfESC")
    pspict.dilatation(3)

    A=Point(0,0)
    B=Point(2,2)
    cer=CircleAB(A,B)
    C=cer.get_point(-90)

    trig=Polygon(A,B,C)
    trig.put_mark(0.4,pspict=pspict)

    trig.edges[0].put_mark(0.2,angle=None,added_angle=0,text="\SI{122.7}{\centi\meter}",automatic_place=(pspict,""))
    trig.edges[1].put_mark(0.2,angle=None,added_angle=0,text="\SI{130.2}{\centi\meter}",automatic_place=(pspict,""))
    trig.edges[2].put_mark(0.2,angle=None,added_angle=0,text="\SI{127.4}{\centi\meter}",automatic_place=(pspict,""))

    rh=RightAngleAOB(A,C,B)

    no_symbol(trig.vertices)
    pspict.DrawGraphs(trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
