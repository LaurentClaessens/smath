# -*- coding: utf8 -*-
from phystricks import *
def JRCJooPHFcKn():
    pspict,fig = SinglePicture("JRCJooPHFcKn")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(5,0)
    F=Segment(A,B).midpoint()
    K=Point(2,1)

    E=F.projection(  Segment(A,K) )
    C=B.projection(  Segment(A,K) )

    gtriangle=Polygon(A,B,C)
    ptriangle=Polygon(A,F,E)

    gtriangle.put_mark(0.2,pspict=pspict)
    ptriangle.put_mark(0.2,text_list=["\( A\)","\( F\)","\( E\)"],pspict=pspict)
    gtriangle.edges[0].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)

    rh1=RightAngle( Segment(E,F),Segment(A,C),0.3,1,0 )
    rh2=RightAngle( Segment(C,B),Segment(A,C),0.3,0,0 )

    mes1=Segment(A,E).get_measure(-0.4,0.1,None,"\SI{3.2}{\centi\meter}",automatic_place=(pspict,"corner"))
    mes2=Segment(E,C).get_measure(-0.4,0.1,None,"\SI{3.5}{\centi\meter}",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(gtriangle,ptriangle,rh1,rh2,mes1,mes2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
