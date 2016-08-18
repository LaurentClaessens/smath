# -*- coding: utf8 -*-
from phystricks import *
def YBWRooQjwZuu():
    pspict,fig = SinglePicture("YBWRooQjwZuu")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,1)
    M=Segment(A,B).midpoint()
    cer=CircleOA(M,A)
    C=cer.get_point(90)
    #D=cer.get_point(Segment(A,B).angle()-30)
    D=Point(B.x,A.y)
    
    trig1=Polygon(A,B,C)
    trig2=Polygon(A,B,D)

    M.put_mark(0.2,angle=None,added_angle=0,text="\( M\)",pspict=pspict)

    trig1.edges[0].divide_in_two(n=2,d=0.1,l=0.2,angle=45,pspict=pspict)

    trig1.put_mark(0.2,points_names="ABC",pspict=pspict)
    trig2.put_mark(0.2,points_names="  D",pspict=pspict)

    rh1=RightAngleAOB(A,C,B)
    rh2=RightAngleAOB(A,D,B)

    no_symbol(trig1.vertices,D)
    pspict.DrawGraphs(M,trig1,trig2,rh1,rh2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
