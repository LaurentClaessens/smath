# -*- coding: utf8 -*-
from phystricks import *
def DEAXooTRICJi():
    pspict,fig = SinglePicture("DEAXooTRICJi")
    pspict.dilatation(0.6)

    A=Point(0,0)
    B=A+(4,0)
    O=Segment(A,B).midpoint()
    cer=CircleOA(O,A).graph(0,180)

    AB=Segment(A,B)
    AB.divide_in_two(n=2,d=0.1,l=0.3,pspict=pspict)

    T=cer.get_point(90+60)
    R=cer.get_point(40)

    A.put_mark(0.2,angle=180+45,added_angle=0,text="\( A\)",pspict=pspict)
    B.put_mark(0.2,angle=-45,added_angle=0,text="\( B\)",pspict=pspict)
    T.put_mark(0.2,angle=None,added_angle=0,text="\( T\)",pspict=pspict)
    R.put_mark(0.2,angle=None,added_angle=0,text="\( R\)",pspict=pspict)

    no_symbol(A,B)
    pspict.DrawGraphs(cer,A,B,T,R,O,AB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
