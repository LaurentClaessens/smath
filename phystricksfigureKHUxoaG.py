# -*- coding: utf8 -*-
from phystricks import *
def figureKHUxoaG():
    pspict,fig = SinglePicture("figureKHUxoaG")
    pspict.dilatation(1)

    M=Point(0,0)
    cer=Circle(M,2)

    a=80
    b=20
    A=cer.get_point(a)
    D=cer.get_point(b)
    B=cer.get_point(b+180)
    C=cer.get_point(a+180)

    A.put_mark(0.2,None,"\( A\)",pspict=pspict)
    B.put_mark(0.2,None,"\( B\)",pspict=pspict)
    C.put_mark(0.2,None,"\( C\)",pspict=pspict)
    D.put_mark(0.2,None,"\( D\)",pspict=pspict)
    M.put_mark(0.2,120,"\( M\)",pspict=pspict)


    d1=Segment(A,C)
    d2=Segment(D,B)

    l1=Segment(A,D)
    l2=Segment(B,C)
    l1.parameters.style="dashed"
    l2.parameters.style="dashed"
    l1.parameters.color="red"
    l2.parameters.color="red"

    pspict.DrawGraphs(A,B,C,D,M,cer,l1,l2,d1,d2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
