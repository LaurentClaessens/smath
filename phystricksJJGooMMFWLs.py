# -*- coding: utf8 -*-
from phystricks import *
def JJGooMMFWLs():
    pspict,fig = SinglePicture("JJGooMMFWLs")
    pspict.dilatation(0.1)

    C=Point(0,0)
    A=Circle(C,5).get_point( (180+30)*degree )
    B=Circle(C,12).get_point( (180+30-90)*degree )

    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,90,"\( B\)",pspict=pspict,position="S")
    C.put_mark(0.2,0,"\( C\)",pspict=pspict,position="W")

    rh=RightAngle(  Segment(C,A),Segment(C,B),1,1 )

    trig=Polygon(A,B,C)
    trig.edges[0].put_mark(0.2,trig.edges[0].advised_mark_angle(pspict)*degree,"\( 13\)",pspict=pspict,position="corner")
    trig.edges[1].put_mark(0.2,None,"\( 12\)",pspict=pspict,position="corner")
    trig.edges[2].put_mark(0.2,None,"\( ?\)",pspict=pspict,position="corner")

    no_symbol(trig.vertices)

    pspict.DrawGraphs(A,B,C,trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
