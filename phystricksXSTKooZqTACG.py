# -*- coding: utf8 -*-
from phystricks import *
def XSTKooZqTACG():
    pspict,fig = SinglePicture("XSTKooZqTACG")
    pspict.dilatation(0.7)

    A=Point(0,0)
    B=Point(0,-2)
    C=Point(4,-2)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    triangle.edges[0].put_mark(0.2,triangle.edges[0].advised_mark_angle(pspict)+180,"\( 6\)",pspict=pspict,position="E")
    triangle.edges[1].put_mark(0.2,triangle.edges[1].advised_mark_angle(pspict)+180,"\( 8\)",pspict=pspict,position="N")
    triangle.edges[2].put_mark(0.2,triangle.edges[2].advised_mark_angle(pspict)+180,"\( 10\)",pspict=pspict,position="corner")

    rh=RightAngle(  triangle.edges[0],triangle.edges[1],0,1 )

    pspict.DrawGraphs(triangle,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
