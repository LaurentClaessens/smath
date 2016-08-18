# -*- coding: utf8 -*-
from phystricks import *
def YBxSjFS():
    pspict,fig = SinglePicture("YBxSjFS")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    A=Point(-3,6)
    O=Point(0,0)
    k=Segment(A,O)
    B=k.get_point(2)
    C=Point(10,1)

    s1=Segment(A,B)
    s2=Segment(B,C)

    A.put_mark(0.2,90,"\( A\)",pspict=pspict,position="S")
    B.put_mark(0.2,-90,"\( B\)",pspict=pspict,position="N")
    C.put_mark(0.2,90,"\( C\)",pspict=pspict,position="S")


    pspict.DrawGraphs(s1,s2,A,B,C)
    pspict.axes.single_axeX.Dx=2
    pspict.axes.single_axeY.Dx=2
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
