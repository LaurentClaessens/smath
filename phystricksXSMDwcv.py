# -*- coding: utf8 -*-
from phystricks import *
def XSMDwcv():
    pspict,fig = SinglePicture("XSMDwcv")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(x/2+3).graph(-2,5)

    P=Point(0,f(0))
    OP=Segment(  Point(0,0),P )
    measure_p=MeasureLength(OP,0.3)
    measure_p.put_mark(0.2,measure_p.advised_mark_angle(pspict),"\( p\)",pspict=pspict)

    A=f.get_point(1)
    B=f.get_point(3)
    M=Point(B.x,A.y)
    M.put_mark(0.2,-45,"\( M\)",pspict=pspict)

    A.put_mark(0.2,90,"\( A\)",pspict=pspict)
    B.put_mark(0.2,90,"\( B\)",pspict=pspict)

    BM=Segment(B,M)
    BM.put_mark(0.2,0,"\( \Delta y\)",pspict=pspict)
    AM=Segment(A,M)
    AM.put_mark(-0.3,AM.advised_mark_angle(pspict),"\( \Delta x\)",pspict=pspict)

    pspict.math_BB.append(Point(0,0),pspict)

    pspict.comment="The grid goes from (-2,0) to (5,6). Id est, it contains (0,0)"
    pspict.DrawGraphs(f,A,B,M,BM,AM,measure_p)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
