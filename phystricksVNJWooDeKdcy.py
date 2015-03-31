# -*- coding: utf8 -*-
from phystricks import *
def VNJWooDeKdcy():
    pspict,fig = SinglePicture("VNJWooDeKdcy")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    T=Point(0,0)
    S=Point(1,2)
    U=Circle(   Segment(T,S).midpoint() ).get_point(30)

    trig=Polygon(S,T,Y)
    trig.put_mark(0.2,points_names="STU",pspict=pspict)
    rh=RightAngleAOB(S,U,T)

    pspict.DrawGraphs(trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
