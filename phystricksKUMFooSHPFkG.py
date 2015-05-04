# -*- coding: utf8 -*-
from phystricks import *
def KUMFooSHPFkG():
    pspict,fig = SinglePicture("KUMFooSHPFkG")
    pspict.dilatation(1)


    A=Point(0,0)
    B=Circle(A,5).get_point(20)
    D=Segment(A,B).rotation(-90).F
    C=Segment(D,A).rotation(-90).F

    carre=Polygon(A,B,C,D)
    carre.put_mark(0.4,pspict=pspict)

    E=CircleOA(  Segment(A,B).midpoint(),   A    ).get_point(70)
    trig=Polygon(A,B,E)

    E.put_mark(0.2,90,"\( E\)",automatic_place=(pspict,""))

    mes_car=[    s.get_code( n=1,d=0.1,l=0.3,angle=45,pspict=pspict ) for s in carre.edges     ]

    rh=RightAngle( Segment(A,E),Segment(E,B),0,1  )
    rhc1=RightAngle( Segment(A,B),Segment(A,D),1,1  )
    rhc2=RightAngle( Segment(A,B),Segment(B,C),0,1  )

    mesAE=trig.edges[1].get_mark(0.1,angle=trig.edges[1].advised_mark_angle(pspict)+180,text="\( 2\)",mark_point=None,automatic_place=pspict)
    mesEB=trig.edges[2].get_mark(0.1,angle=trig.edges[2].advised_mark_angle(pspict)+180,text="\( 7\)",mark_point=None,automatic_place=pspict)

    for p in [A,B,C,D,E]:
        p.parameters.symbol=""

    pspict.DrawGraphs(carre,trig,mes_car,rh,E,mesAE,mesEB,rhc1,rhc2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
