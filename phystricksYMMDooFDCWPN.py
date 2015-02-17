# -*- coding: utf8 -*-
from phystricks import *
def YMMDooFDCWPN():
    pspict,fig = SinglePicture("YMMDooFDCWPN")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    L=5
    A=Point(0,0)
    B=Point(L,0)
    P=Segment(A,B).get_point_proportion(0.3)

    A.put_mark(0.2,angle=-90,text="\( 0\)",automatic_place=(pspict,""))
    B.put_mark(0.2,angle=-90,text="\( 10\)",automatic_place=(pspict,""))
    P.put_mark(0.2,angle=-90,text="\( x\)",automatic_place=(pspict,""))

    C1=CircleAB(A,P).graph(0,180)
    C2=CircleAB(P,B).graph(0,180)
    C3=CircleAB(A,B).graph(0,180)

    seg=Segment(A,B)
    seg.parameters.style='dashed'

    pspict.DrawGraphs(C1,C2,C3,seg,A,B,P)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
