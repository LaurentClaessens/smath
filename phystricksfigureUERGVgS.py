# -*- coding: utf8 -*-
from phystricks import *
def figureUERGVgS():
    pspict,fig = SinglePicture("figureUERGVgS")
    pspict.dilatation(0.7)

    x=var('x')
    f=phyFunction(3*x/4+3).graph(-3,4)

    B=Point(0,f(0))
    B.put_mark(0.2,180,"\( b\)",automatic_place=pspict)
    A=Point(1,f(1))
    X=Point(1,f(0))
    seg=Segment(B,X)
    seg.parameters.style="dashed"

    measure=MeasureLength(Segment(X,A),0.1)
    measure.put_mark(0.2,0,"\( a\)",automatic_place=pspict)

    I=Point(1,0)
    O=Point(0,0)
    J=Point(0,1)

    I.put_mark(0.2,-90,"\( I\)",automatic_place=pspict)
    J.put_mark(0.2,180,"\( J\)",automatic_place=pspict)
    O.put_mark(0.2,90+14,"\( O\)",automatic_place=pspict)

    pspict.DrawGraphs(f,I,J,O,B,seg,measure)

    pspict.axes.no_numbering()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
