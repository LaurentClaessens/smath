# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *

def UEqUrvi():
    pspict,fig = SinglePicture("UEqUrvi")
    pspict.dilatation(2)

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

    M=Segment(A,B).center()
    ama=M.advised_mark_angle
    #M=M+(0,0.1)

    G=M+(0,-lo/3)
    P=G.projection(Segment(A,C))

    decomp=Polygon(M,G,P)
    decomp.parameters.color="blue"

    M.put_mark(0.2,ama,"\( M\)",automatic_place=pspict)
    P.put_mark(0.2,ama,"\( P\)",automatic_place=pspict)
    G.put_mark(0.2,0,"\( G\)",automatic_place=pspict)

    pspict.DrawGraphs(A,B,C,M,trig,angle,decomp)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
