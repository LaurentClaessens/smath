# -*- coding: utf8 -*-
from phystricks import *
def UKTooJhUzKU():
    pspict,fig = SinglePicture("UKTooJhUzKU")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    K=Point(0,0)
    L=Point(10,0)

    M1=Circle(K,1).get_point(20)
    M2=Circle(L,1).get_point(170)

    M1.put_mark(0.2,M1.advised_mark_angle,"\( M?\)",automatic_place=(pspict,"corner"))
    M2.put_mark(0.2,M2.advised_mark_angle,"\( M?\)",automatic_place=(pspict,"corner"))

    K.put_mark(0.2,180+45,"\( K\)",automatic_place=(pspict,"corner"))
    L.put_mark(0.2,-45,"\( L\)",automatic_place=(pspict,"corner"))

    KL=Segment(K,L)
    KM1=Segment(K,M1)
    LM2=Segment(L,M2)

    KL.put_mark(0.2,-90,"\( 10\)",automatic_place=(pspict,"N"))
    KM1.put_mark(0.2,KM1.advised_mark_angle,"\( 1\)",automatic_place=(pspict,"corner"))
    LM2.put_mark(0.2,LM2.advised_mark_angle+180,"\( 1\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(K,L,M1,M2,KL,KM1,LM2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
