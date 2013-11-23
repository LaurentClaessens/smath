# -*- coding: utf8 -*-
from phystricks import *
def BZRzIsR():
    pspict,fig = SinglePicture("BZRzIsR")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.3)

    s1=Segment(  Point(0,20),Point(8,12) )
    s2=Segment(Point(0,0),Point(8,20))
    
    pspict.DrawGraphs(s1,s2)

    pspict.axes.single_axeY.Dx=2

    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
