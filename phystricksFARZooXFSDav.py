# -*- coding: utf8 -*-
from phystricks import *
def FARZooXFSDav():
    pspict,fig = SinglePicture("FARZooXFSDav")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    K=Point(0,0)
    L=Point(4,0)
    M=Point(1,3)

    S=Point(M.x,K.y)
    trig=Polygon(K,L,M)
    trig.put_mark(0.2,points_names="KLM",pspict=pspict)
    hauteur=Segment(M,S)
    rh=RightAngle(hauteur,Segment(K,L),0.2,0,0)

    hauteur.put_mark(0.2,angle=None,text="\( 8\)",automatic_place=(pspict,""))
    mx=Segment(S,K).get_mark(0.2,angle=None,text="\( x\)",automatic_place=(pspict,""))
    m5=Segment(L,S).get_mark(0.2,angle=None,text="\( 5\)",automatic_place=(pspict,""))

    no_symbol(K,L,M)

    pspict.DrawGraphs(trig,hauteur,rh,mx,m5)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
