# -*- coding: utf8 -*-
from phystricks import *
def RRWJooIPQhTn():
    pspicts,figs = IndependentPictures("RRWJooIPQhTn",4)

    for psp in pspicts:
        psp.dilatation(1)

    A=Point(0,0)
    B=Point(3,0)
    C=Point(0,2)
    trig=Polygon(A,B,C)
    trig.put_mark(0.2,points_names="ABC",pspict=pspicts)
    rh=RightAngleAOB(C,A,B)
    trig.edges[0].put_mark(0.2,angle=None,added_angle=180,text="\( 5\)",automatic_place=(pspicts,""))
    trig.edges[2].put_mark(0.2,angle=None,added_angle=180,text="\( 3\)",automatic_place=(pspicts,""))
    no_symbol(trig.vertices)

    pspicts[0].DrawGraphs(trig,rh)


    D=Point(0,0)
    E=Point(4,0)
    F=E+(2,-2)
    G=D+F-E
    H=Point(G.x,D.y)
    H.put_mark(0.2,angle=90,added_angle=0,text="\( H\)",automatic_place=(pspicts,""))
    parall=Polygon(D,E,F,G)
    parall.put_mark(0.2,points_names="DEFG",pspict=pspicts)
    hauteur=Segment(H,G)
    hauteur.parameters.style='dashed'
    rh=RightAngleAOB(G,H,E)

    no_symbol(parall.vertices,H)
    pspicts[1].DrawGraphs(parall,hauteur,rh,H)


    K=Point(0,0)
    L=Point(2,0)
    M=Point(1.5,2)
    S=Point(M.x,K.y)
    S.put_mark(0.2,angle=-90,added_angle=0,text="\( S\)",automatic_place=(pspicts,""))
    trig=Polygon(K,L,M)
    trig.put_mark(0.2,points_names="KLM",pspict=pspicts)
    hauteur=Segment(M,S)
    hauteur.parameters.style='dashed'
    rh=RightAngleAOB(K,S,M)

    no_symbol(trig.vertices,S)
    pspicts[2].DrawGraphs(trig,hauteur,rh,S)


    H=Point(0,0)
    I=Point(1.5,3)
    J=Point(2.5,-0.5)

    T=J.projection(Segment(H,I))

    T.put_mark(0.2,angle=None,added_angle=0,text="\( T\)",automatic_place=(pspicts,""))
    trig=Polygon(H,I,J)
    trig.put_mark(0.2,points_names="HIJ",pspict=pspicts)
    hauteur=Segment(T,J)
    hauteur.parameters.style='dashed'
    rh=RightAngleAOB(J,T,I)

    no_symbol(trig.vertices,T)
    pspicts[3].DrawGraphs(trig,hauteur,rh,T)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
