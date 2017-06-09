# -*- coding: utf8 -*-
from phystricks import *
def FSSAooLvkqAf():
    pspict,fig = SinglePicture("FSSAooLvkqAf")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1.5)
    pspict.rotation(24)

    K=Point(0,0)
    L=Point(4,0)
    M=Point(3,3)

    trig1=Polygon(K,L,M)
    trig1.put_mark(0.2,points_names="KLM",pspict=pspict)

    parall=[]

    for i in [0,1,2]:
        S=trig1.edges[i].midpoint()
        Sp=S.translate(trig1.edges[i].orthogonal().fix_size(0.7))
        s1=Segment(S,Sp)
        s1.parameters.style='dashed'
        s1.put_code(n=2,l=0.2,d=0.05,pspict=pspict)
        p1=trig1.edges[i].parallel_trough(Sp).dilatation(2)
        parall.append(p1)
        rh1=RightAngleAOB(  trig1.edges[i].I,S,Sp,r=0.2  )
        rh2=RightAngleAOB(  p1.I,Sp,S ,r=0.2 )
        pspict.DrawGraphs(s1,rh1,rh2)

    A=Intersection(  parall[0],parall[1] )[0]
    B=Intersection(  parall[1],parall[2] )[0]
    C=Intersection(  parall[2],parall[0] )[0]

    trig2=Polygon(A,B,C)
    trig2.put_mark(0.2,points_names="ABC",pspict=pspict)

    no_symbol(trig1.vertices,trig2.vertices)
    pspict.DrawGraphs(trig1,trig2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
