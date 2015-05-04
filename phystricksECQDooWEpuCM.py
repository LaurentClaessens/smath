# -*- coding: utf8 -*-
from phystricks import *
def ECQDooWEpuCM():
    pspict,fig = SinglePicture("ECQDooWEpuCM")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)


    A=Point(0,0)
    B=Point(4,-1)
    C=Point(4,2)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,["$A$","$B$","$C$"],pspict=pspict)

    hauteur=triangle.edges[1].orthogonal_trough(A).dilatation(1.4)
    rh=RightAngle(hauteur,triangle.edges[1],0,1)

    pspict.DrawGraphs(triangle,hauteur,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
