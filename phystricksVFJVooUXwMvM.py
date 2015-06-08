# -*- coding: utf8 -*-
from phystricks import *
def VFJVooUXwMvM():
    pspict,fig = SinglePicture("VFJVooUXwMvM")
    pspict.dilatation(1)

    h=2
    l=7
    s=2.6
    A=Point(0,0)
    D=Point(A.x,-h)
    B=A+(l,0)
    C=Point(B.x,D.y)
    E=Point(s,A.y)
    F=Point(E.x,D.y)

    F.put_mark(0.2,angle=-90,added_angle=0,text="\( F\)",automatic_place=(pspict,""))

    rect=Polygon(A,B,C,D)
    rect.put_mark(0.2,points_names="ABCD",pspict=pspict)
    rect.edge.parameters.style="dashed"

    #rect.edges[2].put_measure(measure_distance=-0.5,mark_distance=0.3,mark_angle=-90,name="\SI{8}{\centi\meter}",automatic_place=(pspict,""))
    #rect.edges[1].put_measure(measure_distance=-0.5,mark_distance=0.5,mark_angle=0,name="\SI{3}{\centi\meter}",automatic_place=(pspict,""))

    trig=Polygon(D,E,C)
    trig.put_mark(0.2,points_names=" E ",pspict=pspict)

    hauteur=Segment(E,F)
    rh=RightAngleAOB(E,F,C)

    no_symbol(rect.vertices,E,F)
    pspict.DrawGraphs(trig,rect,hauteur,rh,F)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
