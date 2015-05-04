# -*- coding: utf8 -*-
from phystricks import *
def SQRooAWmMQL():
    pspict,fig = SinglePicture("SQRooAWmMQL")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    carre=Polygon(Point(0,0),Point(1,0),Point(0.8,1),Point(0,1))

    angle1=RightAngle(  carre.edges[2] ,carre.edges[3],0,1 )
    angle2=RightAngle(  carre.edges[3] ,carre.edges[0],0,1 )

    #angle1.parameters.color="blue"
    #angle2.parameters.color="red"

    pspict.DrawGraphs(carre,angle1,angle2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
