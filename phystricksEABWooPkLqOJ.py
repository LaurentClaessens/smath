# -*- coding: utf8 -*-
from phystricks import *
def EABWooPkLqOJ():
    pspict,fig = SinglePicture("EABWooPkLqOJ")
    pspict.dilatation(0.8)

    P=Point(0,0)
    H=P+(4,0)
    N=Segment(P,H).midpoint()
    cer1=CircleOA(N,P).graph(0,180)
    cer2=CircleAB(H,N).graph(0,180)

    G=cer1.get_point(180-50)
    HG=Segment(H,G).dilatation(1.3)
    K=Intersection(HG,cer2)[0]

    PH=Segment(P,H)
    PH.divide_in_two(n=2,d=0.1,l=0.3,pspict=pspict)

    P.put_mark(0.2,angle=180+45,added_angle=0,text="\( P\)",pspict=pspict)
    H.put_mark(0.2,angle=-45,added_angle=0,text="\( H\)",pspict=pspict)
    K.put_mark(0.2,angle=None,added_angle=0,text="\( K\)",pspict=pspict)
    G.put_mark(0.2,angle=None,added_angle=0,text="\( G\)",pspict=pspict)
    N.put_mark(0.2,angle=-90,added_angle=0,text="\( N\)",pspict=pspict)

    no_symbol(P,H,N,K,G)
    pspict.DrawGraphs(cer1,cer2,P,H,G,K,N,PH,HG)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
