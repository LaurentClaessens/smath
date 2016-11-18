# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *

def UEqUrvi():
    pspict,fig = SinglePicture("UEqUrvi")
    pspict.dilatation(0.8)

    alpha=30
    A=Point(0,0)
    lo=4
    C=Circle( A,lo ).get_point(alpha)
    B=Point(C.x,0)
    trig=Polygon(A,B,C)

    A.put_mark(0.2,180,"\( A\)",pspict=pspict)
    B.put_mark(0.2,00,"\( B\)",pspict=pspict)
    C.put_mark(0.2,90,"\( C\)",pspict=pspict)

    angle=AngleAOB(B,A,C)
    angle.put_mark(text="\( {}\)".format(str(alpha)),pspict=pspict)

    P=B.projection(Segment(A,C),advised=True)
    P.put_mark(0.2,P.advised_mark_angle(pspict),"\( P\)",pspict=pspict)

    BP=Segment(P,B)
    BP.parameters.style="dashed"

    pspict.DrawGraphs(A,B,C,P,trig,BP,angle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
