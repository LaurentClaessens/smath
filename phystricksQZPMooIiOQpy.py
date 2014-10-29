# -*- coding: utf8 -*-
from phystricks import *
def QZPMooIiOQpy():
    pspict,fig = SinglePicture("QZPMooIiOQpy")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(4,1)
    C=Point(2.5,3)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)
    
    for i in [0,1,2]:
        P=triangle.vertices[i]
        cot=triangle.edges[ (i+1)%3 ]
        hauteur=cot.orthogonal_trough(P).dilatation(1.5)
        rh=RightAngle(hauteur,cot,0.2,0,0)
        pspict.DrawGraphs(hauteur,rh)

    pspict.DrawGraphs(triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
