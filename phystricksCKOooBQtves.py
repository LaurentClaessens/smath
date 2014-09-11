# -*- coding: utf8 -*-
from phystricks import *
def CKOooBQtves():
    pspictA,figA = SinglePicture("EIQooXptWUa")
    pspictB,figB = SinglePicture("GUEooKQcWgv")
    pspictC,figC = SinglePicture("MQJooVtXTde")

    pspicts=[pspictA,pspictB,pspictC]
    figs=[figA,figB,figC]

    for psp in pspicts :
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.5)

    l=10
    a1=40
    a2=75

    A=Point(0,0)
    B=Point(l,0)

    seg1=Segment(A,B).dilatation(1.3)
    A.put_mark(0.2,180+45,"\( A\)",automatic_place=(pspicts,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspicts,"corner"))
    
    m=Segment(A,B).center()
    m.parameters.symbol=""
    m.put_mark(0.2,-90,"\( {}\)".format(l),automatic_place=(pspicts,"N"))


    K=Circle(A,12).get_point(a1)
    L=Circle(B,9).get_point(180-a2)

    seg2=Segment(A,K)
    seg3=Segment(B,L)

    seg2.parameters.style='dashed'
    seg3.parameters.style='dashed'

    C=Intersection(seg2,seg3)[0]
    C.put_mark(0.2,90,"\( C\)",automatic_place=(pspicts,"S"))

    angle1=Angle(B,A,K)
    angle2=Angle(L,B,A)

    angle1.put_mark(0.2,angle1.advised_mark_angle,"\( {}\)".format(a1),automatic_place=(pspicts,""))
    angle2.put_mark(0.2,angle2.advised_mark_angle,"\( {}\)".format(a2),automatic_place=(pspicts,''))

    edge1=Segment(A,B)
    edge2=Segment(A,C)
    edge3=Segment(B,C)

    pspicts[0].DrawGraphs(A,B,seg1,m)
    pspicts[1].DrawGraphs(A,B,seg1,seg2,seg3,angle1,angle2,m)
    pspicts[2].DrawGraphs(A,B,C,angle1,angle2,edge1,edge2,edge3,m)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()