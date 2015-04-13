# -*- coding: utf8 -*-
from phystricks import *
def ZJATooXEJmyI():
    pspict,fig = SinglePicture("ZJATooXEJmyI")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,-1)
    C=Segment(B,A).orthogonal().dilatation(0.34).F

    rh=RightAngleAOB(A,B,C)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,points_names="SRT",pspict=pspict)

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
