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
    measure_p.put_mark(0.2,measure_p.advised_mark_angle(pspict),"\( p\)",automatic_place=pspict)

    A=f.get_point(1)
    B=f.get_point(3)
    M=Point(B.x,A.y)
    M.put_mark(0.2,-45,"\( M\)",automatic_place=pspict)

    A.put_mark(0.2,90,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,90,"\( B\)",automatic_place=pspict)

    BM=Segment(B,M)
    BM.put_mark(0.2,0,"\( \Delta y\)",automatic_place=pspict)
    AM=Segment(A,M)
    AM.put_mark(-0.2,AM.advised_mark_angle(pspict),"\( \Delta x\)",automatic_place=pspict)

    pspict.DrawGraphs(f,A,B,M,BM,AM,measure_p)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
