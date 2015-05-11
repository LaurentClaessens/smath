# -*- coding: utf8 -*-
from phystricks import *
def BODTooGUhQDy():
    pspicts,figs = IndependentPictures("BODTooGUhQDy",3)

    for psp in pspicts:
        psp.dilatation(1)

    A=Point(0,0)
    B=Point(2.5,0)
    C=Point(1,2)

    trig=[Polygon(A,B,C),Polygon(A,B,C),Polygon(A,B,C)]
    for tr in trig:
        tr.put_mark(0.2,pspict=pspicts)
        no_symbol(tr.vertices)

    
    J=Segment(B,A).midpoint()
    med=Segment(C,J)
    trig[0].edges[0].divide_in_two(n=2,d=0.1,l=0.2,angle=45,pspict=pspicts)
    J.put_mark(0.2,angle=None,added_angle=0,text="\( J\)",automatic_place=(pspicts,""))
    pspicts[0].DrawGraphs(J,med,trig[0])

    H=C.projection(Segment(A,B))
    hauteur=Segment(C,H)
    hauteur.parameters.style="dashed"
    rh=RightAngleAOB(C,H,A)

    hauteur.divide_in_two(n=2,d=0.1,l=0.2,angle=45,pspict=pspicts)
    K=hauteur.midpoint()
    K.put_mark(0.2,angle=45,added_angle=0,text="\( K\)",automatic_place=(pspicts,""))
    tr2=Polygon(A,K,B)
    #tr2.put_mark(0.2,points_names=" K ",pspict=pspicts)

    pspicts[1].DrawGraphs(hauteur,rh,trig[1],tr2,K)

    R=K+(2,0)
    L=Intersection( Segment(K,R),Segment(A,C) )[0]
    M=Intersection( Segment(K,R),Segment(B,C) )[0]

    horiz=Segment(L,M)

    pspicts[2].DrawGraphs(hauteur,rh,trig[2],horiz,K)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
