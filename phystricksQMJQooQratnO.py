# -*- coding: utf8 -*-
from phystricks import *
def QMJQooQratnO():
    from communPhys import thales
    pspict,fig = SinglePicture("QMJQooQratnO")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(-0.5,-3)
    C=Point(1.5,-3.5)
    M,P=thales(  A,B,C, 0.52,'A',"B","C","M","P",pspict )

    m1=Segment(A,M).get_mark(0.1,None,"\( 5\)",pspict=pspict,position="corner")
    m2=Segment(P,M).get_mark(-0.1,None,"\( 3\)",pspict=pspict,position="corner")
    m3=Segment(P,B).get_mark(-0.1,None,"\( 2\)",pspict=pspict,position="corner")
    m4=Segment(B,A).get_measure(-0.6,0.1,None,"\( 6\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


