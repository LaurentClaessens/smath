# -*- coding: utf8 -*-
from phystricks import *
def JTQooDUZpht():
    pspict,fig = SinglePicture("JTQooDUZpht")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    A=Point(0,0)
    B=Point(3,1)
    s1=Segment(A,B)
    s2=s1.orthogonal().rotation(180*degree).fix_size(1)

    triangle=Polygon(  s1.I,s1.F,s2.F  )    

    C=s2.F
    A.put_mark(0.2,180  ,"\( A\)",pspict=pspict,position="E")
    B.put_mark(0.2,-30,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,-90,"\( C\)",pspict=pspict,position="N")

    rh=RightAngleAOB(C,A,B)

    pspict.DrawGraphs(triangle,A,B,C,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
