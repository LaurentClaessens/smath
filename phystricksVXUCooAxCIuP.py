# -*- coding: utf8 -*-
from phystricks import *
def VXUCooAxCIuP():
    pspict,fig = SinglePicture("VXUCooAxCIuP")
    pspict.dilatation(1)
    
    l=6
    A=Point(0,0)
    C=Point(l,2)
    D=Point(l,0)

    B=Segment(A,C).get_point_proportion(0.3)
    E=Segment(A,D).get_point_proportion(0.3)

    s1=Segment(B,E)
    trig=Polygon(A,C,D)

    trig.put_mark(0.2,text_list=["\( A\)","\( C\)","\( D\)"],pspict=pspict)
    B.put_mark(0.2,90,"\( B\)",pspict=pspict)
    E.put_mark(0.2,-90,"\( E\)",pspict=pspict)

    for p in trig.vertices:
        p.parameters.symbol=""
    for p in [B,E]:
        p.parameters.symbol=""

    rh1=RightAngleAOB(B,E,A)
    rh2=RightAngle(Segment(A,D),Segment(D,C),0,1)

    pspict.DrawGraphs(trig,s1,rh1,rh2,B,E)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
