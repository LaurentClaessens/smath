# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *

def UEqUrvi():
    pspict,fig = SinglePicture("UEqUrvi")
    pspict.dilatation(1)

    alpha=30
    A=Point(0,0)
    lo=4
    C=Circle( A,lo ).get_point(alpha)
    B=Point(C.x,0)
    trig=Polygon(A,B,C)

    A.put_mark(0.2,180,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,00,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,90,"\( C\)",automatic_place=pspict)

    angle=Angle(B,A,C)
    angle.put_mark(0.2,angle.advised_mark_angle,"\( {}\)".format(str(alpha)),automatic_place=pspict)

    P=B.projection(Segment(A,C),advised=True)
    P.put_mark(0.2,P.advised_mark_angle,"\( P\)",automatic_place=pspict)

    BP=Segment(P,B)
    BP.parameters.style="dashed"

    pspict.DrawGraphs(A,B,C,P,trig,BP,angle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
