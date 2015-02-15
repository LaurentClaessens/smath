# -*- coding: utf8 -*-
from phystricks import *
def RNTRooAXhubs():
    pspict,fig = SinglePicture("RNTRooAXhubs")
    pspict.dilatation(0.5)

    D=Point(0,0)
    E=Point(8,0)
    c1=Circle(D,12)
    c2=Circle(E,6)
    F=Intersection(c1,c2)[1]

    triangle=Polygon(D,E,F)
    triangle.put_mark(0.2,text_list=["\( D\)","\( E\)","\( F\)"],pspict=pspict)

    S=triangle.edges[2].midpoint()
    T=triangle.edges[1].midpoint()
    S.put_mark(0.2,S.advised_mark_angle(pspict)+180,"\( S\)",automatic_place=(pspict,"corner"))
    T.put_mark(0.2,T.advised_mark_angle(pspict)+180,"\( T\)",automatic_place=(pspict,"corner"))

    mes1=Segment(D,S).get_measure(-0.3,0.1,None,"\( 6\)",automatic_place=(pspict,"corner"))
    mes2=Segment(S,F).get_measure(-0.3,0.1,None,"\( 6\)",automatic_place=(pspict,"corner"))
    mes3=Segment(E,T).get_measure(0.3,-0.1,None,"\( 3\)",automatic_place=(pspict,"corner"))
    mes4=Segment(T,F).get_measure(0.3,-0.1,None,"\( 3\)",automatic_place=(pspict,"corner"))
    seg=Segment(S,T)
    seg.put_measure(0.2,0.1,-90,"\( 4\)",automatic_place=(pspict,"N"))
    mes6=Segment(D,E).get_measure(0.3,0.1,-90,"\( ?\)",automatic_place=(pspict,"N"))

    for P in  [D,E,F,S,T]:
        P.parameters.symbol=""


    pspict.DrawGraphs(S,T,triangle,seg,mes1,mes2,mes3,mes4,mes6)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
