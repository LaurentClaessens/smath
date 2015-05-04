# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def KIZooDOXSDH():
    pspict,fig = SinglePicture("KIZooDOXSDH")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(0.8)

    carre=Polygon(Point(0,0),Point(1,1/2),Point(0,5/2),Point(-1,4/2))

    angle1=RightAngle(  carre.edges[0] ,carre.edges[1],0,1)
    angle2=RightAngle(  carre.edges[1] ,carre.edges[2],0,1 )
    angle3=RightAngle(  carre.edges[3] ,carre.edges[0],0,1 )

    #angle1.parameters.color="blue"
    #angle2.parameters.color="red"
    #angle3.parameters.color="green"

    pspict.DrawGraphs(carre,angle1,angle2,angle3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

