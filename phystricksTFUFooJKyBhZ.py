# -*- coding: utf8 -*-
from phystricks import *
def TFUFooJKyBhZ():
    pspict,fig = SinglePicture("TFUFooJKyBhZ")
    pspict.dilatation(0.5)

    B=Point(0,0)
    C=Point(10,0)

    c1=Circle(B,5)
    c2=Circle(C,7)

    A=Intersection(c1,c2)[0]

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    c1.parameters.style="dashed"
    c2.parameters.style="dashed"

    R1=c1.get_point(200)
    R2=c2.get_point(100)

    l1=Segment(B,R1).get_measure(0,0.1,None,"\( 5\)",pspict=pspict,position="corner")
    l2=Segment(C,R2).get_measure(0,0.1,None,"\( 7\)",pspict=pspict,position="corner")

    pspict.DrawGraphs( c1,c2,triangle,l1,l2 )
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
