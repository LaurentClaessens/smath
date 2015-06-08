# -*- coding: utf8 -*-
from phystricks import *
def VEDYooDMnRha():
    pspicts,figs = IndependentPictures("VEDYooDMnRha",2)

    for psp in pspicts:
        psp.dilatation(0.5)
    pspicts[0].rotation(45)
    pspicts[1].rotation(-50)

    A=Point(0,0)
    C=Point(4,0)
    B=Point(C.x,3)

    trig1=Polygon(A,B,C)
    trig1.put_mark(0.2,pspict=pspicts)
    M=trig1.edges[0].midpoint()
    M.put_mark(0.2,angle=None,added_angle=0,text="\( M\)",automatic_place=(pspicts,""))
    MC=Segment(M,C)
    rh=RightAngleAOB(B,C,A)



    S=Point(0,0)
    T=Point(6,0)
    U=Point(T.x,2)

    trig2=Polygon(S,T,U)
    trig2.put_mark(0.2,points_names="STU",pspict=pspicts)

    K=trig2.edges[2].midpoint()
    K.put_mark(0.2,angle=None,added_angle=180,text="\( K\)",automatic_place=(pspicts,""))
    
    trig2.edges[2].divide_in_two(n=2,d=0.1,l=0.4,angle=45,pspict=pspicts)
    rh2=RightAngleAOB(U,T,S)

    KT=Segment(K,T)

    no_symbol(trig1.vertices,K,M,trig2.vertices)
    pspicts[0].DrawGraphs(trig1,rh,MC,M)
    pspicts[1].DrawGraphs(trig2,K,rh2,KT)


    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

