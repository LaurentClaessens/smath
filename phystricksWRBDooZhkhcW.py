# -*- coding: utf8 -*-
from phystricks import *
def WRBDooZhkhcW():
    from communPhys import thales
    pspict,fig = SinglePicture("WRBDooZhkhcW")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    B=Point(0,0)
    A=Point(1,-1)
    C=Point(1.5,3)
    T,S=thales(  C,B,A, 0.73,'C',"B","A","T","S",pspict )

    m1=Segment(S,C).get_mark(0.1,None,"\( 5\)",pspict=pspict,position="corner")
    m2=Segment(T,S).get_mark(0.1,None,"\( 3\)",pspict=pspict,position="corner")
    m3=Segment(B,C).get_measure(-0.6,0.1,None,"\( 13\)",pspict=pspict,position="corner")
    m4=Segment(C,A).get_measure(-0.5,0.1,None,"\( 6.5\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
