# -*- coding: utf8 -*-
from phystricks import *
def CMOooKlzoBL():
    pspict,fig = SinglePicture("CMOooKlzoBL")
    pspict.dilatation(0.5)

    A=Point(0,0)
    B=Point(1.5,0)
    C=Point(1.5,2)

    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,45,"\( C\)",pspict=pspict,position="corner")

    rh=RightAngle( Segment(B,A),Segment(C,B),1,0 )

    trig=Polygon(A,B,C)
    trig.edges[0].put_mark(0.2,text="\( 1.5\)",pspict=pspict,position="N")

    trig.edges[1].put_mark(0.2,text="\( 2\)",pspict=pspict,position="W")
    trig.edges[2].put_mark(0.2,trig.edges[2].advised_mark_angle(pspict)*degree,added_angle=180,text="\( ?\)",pspict=pspict,position="corner")

    no_symbol(trig.vertices)

    pspict.DrawGraphs(A,B,C,trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
