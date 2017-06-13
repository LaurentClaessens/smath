# -*- coding: utf8 -*-
from phystricks import *
def BJOSooIdFKWA():
    from communPhys import thales
    pspict,fig = SinglePicture("BJOSooIdFKWA")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    I=Point(0,0)
    K=Point(-1.5,2)
    J=Point(0.5,2)
    L,M=thales(  I,K,J, 0.65,'I',"K","J","L","M",pspict,rotate=180 )

    m1=Segment(K,J).get_mark(0.1,None,"\( 7\)",pspict=pspict,position="corner")
    m2=Segment(J,L).get_mark(0.1,None,"\( 2\)",pspict=pspict,position="corner")
    m3=Segment(L,I).get_mark(0.1,None,"\( 8\)",pspict=pspict,position="corner")
    m4=Segment(M,I).get_mark(-0.1,None,"\( 5\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

