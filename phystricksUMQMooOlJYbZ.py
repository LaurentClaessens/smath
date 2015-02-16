# -*- coding: utf8 -*-
from phystricks import *
def UMQMooOlJYbZ():
    pspict,fig = SinglePicture("UMQMooOlJYbZ")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.63)

    h=6
    l=8
    p=0.3
    D=Point(0,0)
    A=Point(l,0)
    S=Point(l,h)

    trig=Polygon(D,A,S)
    trig.put_mark(0.4,text_list=[u"départ","\( A\)","sommet"],pspict=pspict)

    trig.edges[1].put_mark(0.2,angle=None,added_angle=180,text="\SI{600}{\meter}",automatic_place=(pspict,""))
    trig.edges[2].put_mark(0.2,angle=None,added_angle=180,text="\SI{1}{\kilo\meter}",automatic_place=(pspict,""))

    Q=Segment(D,S).get_point_proportion(p)
    P=Segment(D,A).get_point_proportion(p)
    P.put_mark(0.2,angle=-90,text="\( P\)",automatic_place=(pspict,""))

    QP=Segment(Q,P)

    rh1=RightAngle(QP,trig.edges[0],0.3,0,0)
    rh2=RightAngle(trig.edges[0],trig.edges[1],0.3,0,1)

    no_symbol(P,trig.vertices)

    pspict.comment="1km and 600m are placed outside the triangle."
    pspict.DrawGraphs(trig,QP,rh1,rh2,P)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

