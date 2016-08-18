# -*- coding: utf8 -*-
from phystricks import *
def NHGWooBOAkGS():
    pspict,fig = SinglePicture("NHGWooBOAkGS")
    pspict.dilatation(4)

    r=1
    K=Point(0,0)
    A=Point(-r,0)
    C=Point(r,0)
    B=Circle( K,r ).get_point(110)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)
    mediat=Segment(B,K)
    mediat.put_mark(0.2,angle=None,added_angle=0,text="\( m\)",pspict=pspict)
    L=Point(B.x,0)

    L.put_mark(0.2,angle=-90,added_angle=0,text="\( L\)",pspict=pspict)
    K.put_mark(0.2,angle=-90,added_angle=0,text="\( K\)",pspict=pspict)

    hauteur=Segment(L,B)
    hauteur.parameters.style="dotted"
    rh=RightAngleAOB(B,L,K)

    no_symbol(A,B,C,L,K)

    pspict.DrawGraphs(trig,mediat,L,K,hauteur,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
