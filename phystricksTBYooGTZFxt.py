# -*- coding: utf8 -*-
from phystricks import *
def TBYooGTZFxt():
    pspict,fig = SinglePicture("TBYooGTZFxt")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    carre=Polygon(Point(0,0),Point(1,0),Point(1,1),Point(0,1))

    angle1=RightAngle(  carre.edges[0] ,carre.edges[1],0,1 )
    angle2=RightAngle(  carre.edges[1] ,carre.edges[2],0,1 )
    angle3=RightAngle(  carre.edges[2] ,carre.edges[3],0,1 )
    angle4=RightAngle(  carre.edges[3] ,carre.edges[0],0,1 )

    #angle1.parameters.color="blue"
    #angle2.parameters.color="red"
    #angle3.parameters.color="green"
    #angle4.parameters.color="cyan"

    pspict.DrawGraphs(carre,angle1,angle2,angle3,angle4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
