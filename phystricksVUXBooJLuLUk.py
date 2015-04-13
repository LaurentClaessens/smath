# -*- coding: utf8 -*-
from phystricks import *
def VUXBooJLuLUk():
    pspict,fig = SinglePicture("VUXBooJLuLUk")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(2,-2)
    C=Segment(A,B).orthogonal().dilatation(0.34).F

    rh=RightAngleAOB(B,A,C)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,points_names="IJK",pspict=pspict)

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
