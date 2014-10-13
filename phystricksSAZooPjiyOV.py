# -*- coding: utf8 -*-
from phystricks import *

def segment_to_carre(seg,color,reverse=False):
    s1=seg.orthogonal()
    iseg=seg.inverse()
    s2=iseg.orthogonal().rotation(180)
    if reverse :
        s1=s1.rotation(180)
        s2=s2.rotation(180)
    poly = Polygon(seg.I,seg.F,s2.F,s1.F)
    poly.parameters.hatched()
    poly.parameters.hatch.color=color
    return poly

def SAZooPjiyOV():
    pspict,fig = SinglePicture("SAZooPjiyOV")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    A=Point(0,0)
    B=Point(3,0)
    C=Point(2.5,2)

    triangle=Polygon(A,B,C)

    c1=segment_to_carre(Segment(A,B),color="red",reverse=True)
    c2=segment_to_carre(Segment(A,C),color="blue")
    c3=segment_to_carre(Segment(B,C),color="cyan",reverse=True)

    c1.parameters.color="red"
    c2.parameters.color="blue"
    c3.parameters.color="cyan"

    pspict.DrawGraphs(c1,c2,c3,triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
