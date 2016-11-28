# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def VNJWooDeKdcy():
    pspict,fig = SinglePicture("VNJWooDeKdcy")
    pspict.dilatation(0.8)

    T=Point(0,0)
    S=Point(3,2)
    ST=Segment(S,T)
    U=Circle(ST.midpoint(), ST.length/2 ).get_point( ST.angle().degree+70)

    trig=Polygon(S,T,U)
    trig.put_mark(0.2,points_names="STU",pspict=pspict)
    rh=RightAngleAOB(S,U,T,r=0.3,n1=0,n2=1)

    angle=AngleAOB(T,S,U)
    angle.put_mark(text="\SI{33}{\degree}",pspict=pspict)

    no_symbol(S,T,U)

    pspict.DrawGraphs(trig,rh,angle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
