# -*- coding: utf8 -*-
from phystricks import *
def CVKooPKKMNG():
    pspict,fig = SinglePicture("CVKooPKKMNG")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    B=Point(0,0)
    C=Point(8,0)

    m1=Circle(B,6).get_point(40)
    m2=Circle(C,6).get_point(180-40)
    s1=Segment(B,m1)
    s2=Segment(C,m2)
    s1.parameters.style="dashed"
    s2.parameters.style="dashed"

    A=Intersection(s1,s2)[0]

    A.put_mark(0.2,90,"\( A\)",pspict=pspict,position="S")
    B.put_mark(0.2,180+45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict,position="corner")

    trig=Polygon(A,B,C)
    for p in trig.vertices:
        p.parameters.symbol=""

    a1=AngleAOB(C,B,A,r=0.5)
    a3=AngleAOB(A,C,B,r=0.5)

    a1.put_mark(0.3,None,"\SI{40}{\degree}",pspict=pspict)
    a3.put_mark(0.3,None,"\SI{40}{\degree}",pspict=pspict)

    pspict.DrawGraphs(A,B,C,s1,s2,trig,a1,a3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
