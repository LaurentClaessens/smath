# -*- coding: utf8 -*-
from phystricks import *
def HHRTooMDylcn():
    pspict,fig = SinglePicture("HHRTooMDylcn")
    pspict.dilatation(0.7)

    A=Point(0,0)
    B=Point(4,2)
    C=Point(3,0)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    K=Segment(A,C).midpoint()
    K.put_mark(0.2,-90,"\( K\)",automatic_place=(pspict,"N"))

    med=Segment(B,K).dilatation(1.3)
    med.parameters.style="dashed"

    pspict.DrawGraphs(triangle,K,med)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
