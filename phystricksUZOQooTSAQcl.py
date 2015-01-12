# -*- coding: utf8 -*-
from phystricks import *
def UZOQooTSAQcl():
    pspict,fig = SinglePicture("UZOQooTSAQcl")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    h=2
    A=Point(0,0)
    B=Point(5,0)
    C=Point(4,h)
    triangle=Polygon(A,B,C)

    triangle.put_mark(0.2,pspict=pspict)
    parallel=(triangle.edges[0]+(0,h)).dilatation(1.5)
    triangle.edges[0]=triangle.edges[0].dilatation(1.3)
    
    a1=Angle(B,A,C)
    a1.put_mark(0.3,a1.advised_mark_angle,"\SI{34}{\degree}",automatic_place=(pspict,"center"))
    a2=Angle(C,B,A)
    a2.put_mark(0.2,a2.advised_mark_angle,"\SI{12}{\degree}",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(triangle,a1,a2,parallel)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
