# -*- coding: utf8 -*-
from phystricks import *
def BJPOooZTVHhi():
    pspict,fig = SinglePicture("BJPOooZTVHhi")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    R=Point(0,0)
    M=Point(7,0)
    Z=Point(6,2)

    A=Segment(R,M).get_point_proportion(0.4)
    I=Segment(R,Z).get_point_proportion(0.4)

    m1=Segment(R,A).get_measure(0.3,-0.1,None,"\( 2\)",automatic_place=(pspict,"corner"))
    m2=Segment(A,M).get_measure(0.3,-0.1,None,"\( 6\)",automatic_place=(pspict,"corner"))

    trig=Polygon(R,Z,M)
    seg=Segment(I,A)
    trig.put_mark(0.2,text_list=["\( R\)","\( Z\)","\( M\)"],pspict=pspict)

    I.put_mark(0.2,None,"\( I\)",automatic_place=(pspict,"corner"))
    A.put_mark(0.2,45,"\( A\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(m1,m2,trig,seg,I,A)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
