# -*- coding: utf8 -*-
from phystricks import *
def APYEkIv():
    pspict,fig = SinglePicture("APYEkIv")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    E=Point(0,0)
    J=Point(5,1)
    K=Point(5,0)

    EK=Segment(E,K)
    KJ=Segment(K,J)

    EK.put_mark(0.2,text="\( 230\)",pspict=pspict,position="N")
    KJ.put_mark(0.2,text="\( 15\)",pspict=pspict,position="W")

    E.put_mark(0.2,text="\( E\)",pspict=pspict,position="N")
    J.put_mark(0.2,text="\( J\)",pspict=pspict,position="W")

    trig=Polygon(E,K,J)

    pspict.DrawGraphs(E,J,trig,EK,KJ)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
