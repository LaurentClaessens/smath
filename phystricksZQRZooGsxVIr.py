# -*- coding: utf8 -*-
from phystricks import *
def ZQRZooGsxVIr():
    pspict,fig = SinglePicture("ZQRZooGsxVIr")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,0)
    C=Point(5,2)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)
    H=Point(C.x,A.y)
    H.put_mark(0.2,angle=-90,added_angle=0,text="\( H\)",pspict=pspict)

    base=Segment(A,H)
    hauteur=Segment(C,H)
    base.parameters.style="dashed"
    hauteur.parameters.style="dashed"

    rh=RightAngleAOB(C,H,A)

    no_symbol(trig.vertices,H)
    pspict.DrawGraphs(base,trig,hauteur,H,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
