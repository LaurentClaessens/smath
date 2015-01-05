# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def IQKJooUmvFBs():
    pspict,fig = SinglePicture("IQKJooUmvFBs")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(5,0)
    C=Point(4,2)

    I=Segment(A,B).proportion(2/3)
    J=Segment(A,C).proportion(2/3)

    IJ=Segment(I,J).dilatation(1.5)
    I.put_mark(0.2,I.advised_mark_angle,"\( I\)",automatic_place=(pspict,"corner"))
    J.put_mark(0.2,J.advised_mark_angle,"\( J\)",automatic_place=(pspict,"corner"))

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    pspict.DrawGraphs(triangle,IJ,I,J)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
