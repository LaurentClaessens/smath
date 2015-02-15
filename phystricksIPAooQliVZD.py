# -*- coding: utf8 -*-
from phystricks import *

def IPAooQliVZD():

    pspictA,figA = SinglePicture("HZPooATdojo")
    pspictB,figB = SinglePicture("JUZooFbAOlx")
    pspictC,figC = SinglePicture("VJZooKxwzhE")
    figs=[figA,figB,figC]
    pspicts=[pspictA,pspictB,pspictC]

    for psp in pspicts :
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.5)

    l1=6
    l2=4
    l3=8

    A=Point(0,0)
    B=Point(l1,0)

    AB=Segment(A,B)

    cer1=Circle(A,l2)
    cer2=Circle(B,l3)

    inter=Intersection(cer1,cer2)
    C1=inter[0]
    C2=inter[1]

    A.put_mark(0.2,180+20,"\( A\)",automatic_place=(pspicts,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspicts,"corner"))
    C1.put_mark(0.2,180+45,"\( C_1\)",automatic_place=(pspicts,"corner"))
    C2.put_mark(0.2,90+45,"\( C_2\)",automatic_place=(pspicts,"corner"))

    Q1=cer1.get_point(45)
    r1=Segment(A,Q1)
    r1.parameters.style="dashed"
    r1.put_mark(0.2,None,"\( {}\)".format(l2),automatic_place=(pspicts,"corner"))

    Q2=cer2.get_point(60)
    r2=Segment(B,Q2)
    r2.parameters.style="dashed"
    r2.put_mark(0.2,None,"\( {}\)".format(l3),automatic_place=(pspicts,"corner"))

    cer1.parameters.color="red"
    r1.parameters.color="red"
    cer2.parameters.color="blue"
    r2.parameters.color="blue"

    a1=C1.angle(origin=A).degree
    a2=C1.angle(origin=B).degree
    petit_rougeC1=cer1.graph(a1-10,a1+10)
    petit_bleuC1=cer2.graph(a2-10,a2+10)


    b1=C2.angle(origin=A).degree
    b2=C2.angle(origin=B).degree
    petit_rougeC2=cer1.graph(b1-10,b1+10)
    petit_bleuC2=cer2.graph(b2-10,b2+10)

    trig1=Polygon(A,B,C1)
    trig2=Polygon(A,B,C2)

    trig1.edge.parameters.style="dashed"
    trig2.edge.parameters.style="dashed"

    m1=Segment(A,C2).center()
    m1.parameters.symbol=""
    m1.put_mark(0.2,None,"\( {}\)".format(l2),automatic_place=(pspicts,"corner"))

    m2=Segment(B,C2).center()
    m2.parameters.symbol=""
    m2.put_mark(0.2,None,"\( {}\)".format(l3),automatic_place=(pspicts,"corner"))

    pspicts[0].DrawGraphs(AB,A,B)
    pspicts[1].DrawGraphs(AB,cer1,cer2,r1,r2,A,B)
    pspicts[2].DrawGraphs(AB,petit_bleuC1,petit_rougeC1,petit_rougeC2,petit_bleuC2,C1,C2,A,B,trig1,trig2,m1,m2)

    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

