# -*- coding: utf8 -*-
from phystricks import *
def UDKYooKlVbjh():
    pspict,fig = SinglePicture("UDKYooKlVbjh")

    A=Point(0,0)
    B=Point(5,1)
    C=Point(2,4)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.3,pspict=pspict)

    K=triangle.edges[2].get_point_proportion(0.7)
    L=triangle.edges[0].get_point_proportion(1-0.7)

    K.put_mark(0.2,180+K.advised_mark_angle(pspict),"\( K\)",pspict=pspict,position="corner")
    L.put_mark(0.2,180+L.advised_mark_angle(pspict),"\( L\)",pspict=pspict,position="corner")

    KL=Segment(K,L)
    KL.put_measure(-0.2,0.2,45,"\( 3\)",pspict=pspict,position="corner")

    mes2=Segment(A,L).get_measure(0.2,0.2,name="\( 2\)",pspict=pspict,position="N")

    pspict.DrawGraphs(triangle,K,L,K,L,mes2,KL)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
