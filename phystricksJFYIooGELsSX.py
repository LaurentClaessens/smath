# -*- coding: utf8 -*-
from phystricks import *
def JFYIooGELsSX():
    pspict,fig = SinglePicture("JFYIooGELsSX")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    lx=6
    ly=4.5
    L=Point(0,0)
    U=L+(lx,0)
    G=U+(0,-ly)
    E=L+(0,-ly)

    rect=Polygon(L,U,G,E)
    rect.put_mark(0.2,text_list=["\( L\)","\( U\)","\( G\)","\( E\)"],pspict=pspict)

    d1=Segment(L,G)
    d2=Segment(E,U)
    O=Intersection(d1,d2)[0]
    O.put_mark(0.2,90,"\( 0\)",automatic_place=(pspict,""))
    for p in [L,U,G,E,O]:
        p.parameters.symbol=""

    a1=Angle(G,L,U,r=0.3)
    a2=Angle(E,L,G)
    a3=Angle(U,G,L)
    a4=Angle(L,G,E,r=0.3)

    l1=Segment(L,U).get_mark(0.2,angle=None,text="\SI{6}{\centi\meter}",automatic_place=(pspict,""))
    l2=Segment(E,L).get_mark(0.2,angle=None,text="\SI{4.5}{\centi\meter}",automatic_place=(pspict,""))

    pspict.DrawGraphs(rect,d1,d2,O,a1,a2,a3,a4,l1,l2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
