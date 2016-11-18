# -*- coding: utf8 -*-
from phystricks import *
def QFpJtQc():
    pspict,fig = SinglePicture("QFpJtQc")
    pspict.dilatation_X(0.6)
    pspict.dilatation_Y(0.6)

    A=Point(0,0)
    B=Point(5,0)
    C=Point(2,3)

    triangle=Polygon(A,B,C)

    M=Segment(A,C).get_point_proportion(0.3)

    s=Segment(C,B).fix_origin(M)
    N=Intersection(s,Segment(A,B))[0]
    t=Segment(A,C).fix_origin(N)
    G=Intersection(t,Segment(C,B))[0]

    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,90,"\( C\)",pspict=pspict,position="S")
    M.put_mark(0.2,M.advised_mark_angle(pspict),"\( M\)",pspict=pspict,position="corner")
    N.put_mark(0.2,text="\( N\)",pspict=pspict,position="N")
    G.put_mark(0.2,Segment(C,B).angle().degree+90,"\( G\)",pspict=pspict,position="corner")

    parallelogram=Polygon(C,G,N,M)

    pspict.DrawGraphs(A,B,C,M,triangle,N,G,parallelogram)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
