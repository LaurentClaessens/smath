# -*- coding: utf8 -*-
from phystricks import *
def BXFFooNyvPYY():
    pspict,fig = SinglePicture("BXFFooNyvPYY")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(0,3)
    C=Point(8,0)
    
    trig=Polygon(A,B,C)
    trig.put_mark(0.4,pspict=pspict)

    trig.edges[1].divide_in_two(n=2,d=0.1,l=0.5,angle=45,pspict=pspict)
    K=trig.edges[1].midpoint()
    mediane=Segment(A,K)
    K.put_mark(0.3,angle=None,added_angle=0,text="\( K\)",automatic_place=(pspict,""))

    trig.edges[0].put_mark(0.2,angle=None,added_angle=0,text="\SI{3}{\centi\meter}",automatic_place=(pspict,""))
    trig.edges[2].put_mark(0.2,angle=None,added_angle=0,text="\SI{8}{\centi\meter}",automatic_place=(pspict,""))

    rh=RightAngleAOB(B,A,C,r=0.5)

    no_symbol(trig.vertices,K)
    pspict.DrawGraphs(trig,K,mediane,K,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
