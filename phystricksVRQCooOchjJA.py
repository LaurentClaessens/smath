# -*- coding: utf8 -*-
from phystricks import *
def VRQCooOchjJA():
    pspict,fig = SinglePicture("VRQCooOchjJA")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(1.5,2.5)
    C=Point(-1,1)

    s1=Segment(A,B)
    s2=s1.parallel_trough(A+(1.5,1))

    I=s1.midpoint()
    J=s2.midpoint()

    sec=Segment(I,J).dilatation(2)

    ang=Angle(s1.F,I,sec.I,r=0.3)
    ang.put_mark(0.2,None,"\SI{140}{\degree}",automatic_place=(pspict,""))

    pspict.DrawGraphs(sec,s1,s2,ang)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

