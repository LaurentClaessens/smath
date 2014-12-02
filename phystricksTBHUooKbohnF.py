# -*- coding: utf8 -*-
from phystricks import *
def TBHUooKbohnF():
    pspicts,figs = IndependentPictures("TBHUooKbohnF",2)
    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    A=Point(0,0)
    B=Point(3,0)
    C=Point(4,4)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspicts)

    I=triangle.edges[0].midpoint()
    J=triangle.edges[1].midpoint()
    K=triangle.edges[2].midpoint()

    IJ=Segment(I,J).dilatation(1.5)
    IK=Segment(I,K).dilatation(1.5)
    KJ=Segment(K,J).dilatation(1.5)

    I.put_mark(0.2,I.advised_mark_angle+180,"\( I\)",automatic_place=(pspicts,"corner"))
    J.put_mark(0.2,J.advised_mark_angle+180,"\( J\)",automatic_place=(pspicts,"corner"))
    K.put_mark(0.2,K.advised_mark_angle+180,"\( K\)",automatic_place=(pspicts,"corner"))


    triangle.edges[0].divide_in_two(n=2,d=0.1,l=0.4,angle=45,pspict=pspicts)
    pspicts[1].DrawGraphs(triangle,IJ,I,J)
    triangle.edges[1].divide_in_two(n=1,d=0.1,l=0.4,angle=45,pspict=pspicts)
    triangle.edges[2].divide_in_two(n=3,d=0.1,l=0.4,angle=45,pspict=pspicts)
    pspicts[0].DrawGraphs(triangle,IJ,IK,KJ,I,J,K)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
