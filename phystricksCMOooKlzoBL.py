# -*- coding: utf8 -*-
from phystricks import *
def CMOooKlzoBL():
    pspict,fig = SinglePicture("CMOooKlzoBL")
    pspict.dilatation(0.5)

    A=Point(0,0)
    B=Point(1.5,0)
    C=Point(1.5,2)

    A.put_mark(0.2,180+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))

    rh=RightAngle( Segment(B,A),Segment(C,B),0.4,0,1 )

    trig=Polygon(A,B,C)
    trig.edges[0].put_mark(0.2,-90,"\( 1.5\)",automatic_place=(pspict,"N"))

    trig.edges[1].put_mark(0.2,0,"\( 2\)",automatic_place=(pspict,"W"))
    trig.edges[2].put_mark(0.2,trig.edges[2].advised_mark_angle*degree+180,"\( ?\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(A,B,C,trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
