# -*- coding: utf8 -*-
from phystricks import *
def IKZEooAwkZSy():
    pspict,fig = SinglePicture("IKZEooAwkZSy")
    pspict.dilatation(1)

    l=5
    h=2
    s=1

    A=Point(0,0)
    B=A+(l,0)
    C=B+(s,-h)
    D=A+(s,-h)

    S=Segment(A,B).get_point_proportion(0.7)
    H=Point(S.x,C.y)
    #H.put_mark(0.2,angle=-90,added_angle=0,text="\( H\)",automatic_place=(pspict,""))

    paral=Polygon(A,B,C,D)
    paral.put_mark(0.2,pspict=pspict)

    paral.edges[2].put_measure(measure_distance=-0.5,mark_distance=0.5,mark_angle=-90,name="base",automatic_place=(pspict,""))

    hauteur=Segment(S,H)
    hauteur.parameters.style="dashed"

    hauteur.put_measure(-0.3,0.2,0,"hauteur",automatic_place=(pspict,""))
    rh=RightAngleAOB(S,H,D)

    no_symbol(paral.vertices)
    pspict.DrawGraphs(paral,hauteur,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
