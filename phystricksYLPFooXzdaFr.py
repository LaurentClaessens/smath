# -*- coding: utf8 -*-
from phystricks import *
def YLPFooXzdaFr():
    pspict,fig = SinglePicture("YLPFooXzdaFr")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    K=Point(0,0)
    M=Point(2.5,0)
    L=Point(M.x,-2)

    trig=Polygon(K,L,M)
    trig.put_mark(0.2,points_names="KLM",pspict=pspict)
    trig.edges[1].put_mark(0.2,angle=0,added_angle=0,text="\SI{9}{\centi\meter}",pspict=pspict)

    ang=AngleAOB(L,K,M)
    ang.put_mark(0.4,angle=None,added_angle=0,text="\SI{34}{\degree}",pspict=pspict)

    rh=RightAngleAOB(L,M,K)

    no_symbol(trig.vertices)
    pspict.DrawGraphs(trig,rh,ang)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
