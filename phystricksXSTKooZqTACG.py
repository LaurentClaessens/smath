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

    triangle.edges[0].put_mark(0.2,triangle.edges[0].advised_mark_angle(pspict)+180,"\( 6\)",automatic_place=(pspict,"E"))
    triangle.edges[1].put_mark(0.2,triangle.edges[1].advised_mark_angle(pspict)+180,"\( 8\)",automatic_place=(pspict,"N"))
    triangle.edges[2].put_mark(0.2,triangle.edges[2].advised_mark_angle(pspict)+180,"\( 10\)",automatic_place=(pspict,"corner"))

    rh=RightAngle(  triangle.edges[0],triangle.edges[1],0.4,0,1 )

    pspict.DrawGraphs(triangle,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
