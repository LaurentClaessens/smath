# -*- coding: utf8 -*-
from phystricks import *
def ZZPQooStuRcw():
    pspict,fig = SinglePicture("ZZPQooStuRcw")
    pspict.dilatation(0.7)

    A=Point(0,0)
    B=A+(6,-2)
    C=A+(-1,-3)

    O=B+(2,1)
    O.put_mark(0.2,180+45,"\( O\)",automatic_place=(pspict,""))

    prime=[ x.symmetric_by(O) for x in [A,B,C] ]
    trig2=Polygon( prime[0],prime[1],prime[2] )
    trig2.put_mark(0.2,text_list=[ "\( A'\)","\( B'\)","\( C'\)" ],pspict=pspict)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)
    rh=RightAngle( trig.edges[0],trig.edges[2],1,0 )

    m1=trig.edges[0].get_mark(0.2,None,"\( 4\)",automatic_place=(pspict,""))
    m2=trig.edges[1].get_mark(0.2,None,"\( 5\)",automatic_place=(pspict,""))
    m3=trig.edges[2].get_mark(0.2,None,"\( 3\)",automatic_place=(pspict,""))

    for p in trig.vertices:
        p.parameters.symbol=""
    for p in trig2.vertices:
        p.parameters.symbol=""

    pspict.DrawGraphs(trig,rh,trig2,m1,m2,m3,O)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
