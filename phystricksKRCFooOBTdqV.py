# -*- coding: utf8 -*-
import string
from phystricks import *
def KRCFooOBTdqV():
    pspict,fig = SinglePicture("KRCFooOBTdqV")
    pspict.dilatation(0.96)


    O=Point(0,0)
    P=Point(4,2)
    Pp=Point(P.x,0)
    seg=Segment(O,P)
    segP=Segment(O,Pp)

    O.parameters.symbol=""

    O.put_mark(0.2,180,"\( O\)",automatic_place=(pspict,""))
    proportions = [0.3,0.6,0.95]
    for i,p in enumerate(proportions) :
        symbol=string.ascii_uppercase[i+11]
        A=seg.get_point_proportion(p)
        Ap=Point(A.x,0)
        A.put_mark(0.2,None,"\( "+symbol+"\)",automatic_place=(pspict,""))
        Ap.put_mark(0.2,-90,"\( "+symbol+"'\)",automatic_place=(pspict,""))
        AAp=Segment(A,Ap)
        rh=RightAngle(  Segment(O,Ap),Segment(Ap,A),0.2, 0,1  )
        for S in [A,Ap]:
            S.parameters.symbol=""
        pspict.DrawGraphs(A,Ap,AAp,rh)

    pspict.DrawGraphs(seg,segP,O)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
