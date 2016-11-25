# -*- coding: utf8 -*-
from phystricks import *
def LWNSooVGvWxJ():
    pspicts,figs = IndependentPictures("LWNSooVGvWxJ",2)

    for psp in pspicts:
        psp.dilatation(1)

    l=2
    A=Point(0,0)
    B=Point(0,l)
    C=Point(l,0)

    trig=Polygon(A,B,C)
    put_equal_lengths_code(trig.edges[0],trig.edges[2],n=1,d=0.1,l=0.3,angle=45,pspicts=pspicts)
    rh=RightAngleAOB(B,A,C)
    trig.put_mark(0.2,pspicts=pspicts)

    no_symbol(trig.vertices)
    pspicts[0].DrawGraphs(trig,rh)


    pspicts[1].dilatation(1)
    K=Point(0,0)
    L=Point(4,2.5)
    KL=Segment(K,L)
    s1=Segment(K,L).rotation(60)
    s2=Segment(L,K).rotation(-25)

    M=Intersection( s1,s2 )[0]

    trig=Polygon(K,L,M)
    trig.put_mark(0.2,points_names="KLM",pspicts=pspicts)

    angK=AngleAOB(L,K,M)
    angK.put_mark(added_angle=0,text="\SI{60}{\degree}",pspicts=pspicts)
    
    angL=AngleAOB(M,L,K)
    angL.put_mark(added_angle=0,text="\SI{25}{\degree}",pspicts=pspicts)

    no_symbol(trig.vertices)
    pspicts[1].DrawGraphs(trig,angK,angL)


    

    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
