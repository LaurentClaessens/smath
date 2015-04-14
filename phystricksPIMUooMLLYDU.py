# -*- coding: utf8 -*-
from phystricks import *
def PIMUooMLLYDU():
    pspict,fig = SinglePicture("PIMUooMLLYDU")
    pspict.dilatation(0.8)

    D=Point(0,0)
    L=Point(12,0)
    K=Point(0,5)
    S1=Point(0,-3)
    S2=Point(-3,0)

    base=Polygon(K,L,D)
    base.put_mark(0.2,points_names="KLD",pspict=pspict)

    base.edges[1].put_mark(0.2,angle=None,added_angle=180,text="\( 12\)",automatic_place=(pspict,""))
    base.edges[2].put_mark(0.2,angle=None,added_angle=180,text="\( 5\)",automatic_place=(pspict,""))

    S1.put_mark(0.3,angle=180+45,text="\( S\)",automatic_place=(pspict,""))
    S2.put_mark(0.3,angle=90+45,text="\( S\)",automatic_place=(pspict,""))

    cot1=Polygon(S1,D,L)
    cot2=Polygon(S2,D,K)
    cot2.edges[0].put_mark(0.2,angle=None,added_angle=180,text="\( 3\)",automatic_place=(pspict,""))

    rh1=RightAngleAOB(S1,D,L,r=0.4,n1=0,n2=1)
    rh2=RightAngleAOB(S2,D,K,r=0.4,n1=0,n2=1)

    N=Intersection(Segment(S2,K),Circle(K,4))[0]
    N.put_mark(0.2,angle=Segment(S2,K).angle()+90,text="\( N\)",automatic_place=(pspict,""))

    P=S1+(0,2)
    P.put_mark(0.2,angle=0,text="\( P\)",automatic_place=(pspict,""))

    measSP=Segment(S1,P).get_measure(-0.3,0.1,None,"\( 2\)",automatic_place=(pspict,""))
    measNK=Segment(N,K).get_measure(-0.3,0.1,None,"\(4\)",automatic_place=(pspict,""))

    no_symbol(K,L,D,S1,S2)

    pspict.DrawGraphs(base,S1,S2,cot1,cot2,rh1,rh2,N,P,measSP,measNK)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
