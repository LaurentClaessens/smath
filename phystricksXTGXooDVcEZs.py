# -*- coding: utf8 -*-
from phystricks import *
def XTGXooDVcEZs():
    pspict,fig = SinglePicture("XTGXooDVcEZs")
    pspict.dilatation(1.4)

    C=Point(1,1)
    A=C+(4,0)
    B=CircleAB(C,A).get_point(66)
    S=Segment(C,A).midpoint()

    trig=Polygon(C,A,B)
    trig.put_mark(0.3,points_names="CAB",pspict=pspict)
    S.put_mark(0.2,angle=-90,added_angle=0,text="\( S\)",pspict=pspict)

    rh=RightAngleAOB(C,B,A)

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,rh,S)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
