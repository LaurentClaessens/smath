# -*- coding: utf8 -*-
from phystricks import *
def QZABooEsqWaq():
    pspict,fig = SinglePicture("QZABooEsqWaq")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    h=2
    A=Point(0,0)
    B=Point(5,0)
    C=Point(4,h)
    triangle=Polygon(A,B,C)

    triangle.put_mark(0.2,pspict=pspict)
    parallel=(triangle.edges[0]+(0,h)).dilatation(1.5)
    triangle.edges[0]=triangle.edges[0]

    for p in triangle.vertices:
        p.parameters.symbol=""
    
    a1=Angle(B,A,C,r=0.5)
    a1.put_mark(0.3,None,"$a$",pspict=pspict)
    a2=AngleAOB(C,B,A,r=0.5)
    a2.put_mark(0.2,None,"$b$",pspict=pspict)
    a3=AngleAOB(A,C,B)
    a3.put_mark(0.2,None,"\( c\)",pspict=pspict)

    pspict.DrawGraphs(triangle,a1,a2,a3,parallel)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
