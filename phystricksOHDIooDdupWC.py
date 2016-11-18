# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def OHDIooDdupWC():
    pspict,fig = SinglePicture("OHDIooDdupWC")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    h=0.5
    L=2
    s=L/5
    O=Point(0,0)
    D=Point(7,0)
    C=D+(L,0)
    B=C+(0,4)
    A=Point(D.x,B.y)
    E=Segment(O,D).get_point_proportion(0.8)
    I=Segment(O,A).get_point_proportion(0.2)
    J=Point(I.x,0)

    O.put_mark(0.2,90+45,"\( O\)",pspict=pspict,position="corner")

    S0=A+(s,0)
    S1=S0+(0,h)
    S2=S1+(s,0)
    S3=S0+(s,0)
    S4=S3+(s,0)
    S5=S2+(s,0)
    S6=S5+(s,0)
    S7=B+(-s,0)

    tour=Polygon(A,S0,S1,S2,S3,S4,S5,S6,S7,B,C,D)
    IJ=Segment(I,J)
    IJ.put_measure(-0.2,0.2,text="\( 2\)",pspict=pspict,position="W")

    ombre=Segment(A,O)
    terrain=Segment(O,D)
    #eau=Segment(E,D)
    #eau.parameters.color='blue'
    #eau.wave(0.2,0.1)

    m2=Segment(O,J).get_measure(0.2,0.2,text="\( 3\)",pspict=pspict,position="N")
    m12=Segment(J,D).get_measure(0.2,0.2,text="\( 12\)",pspict=pspict,position="N")

    pspict.DrawGraphs(O,tour,IJ,ombre,terrain,m2,m12)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

