# -*- coding: utf8 -*-
from phystricks import *
def DefVecteurAXDDGP():
    pspict,fig = SinglePicture("DefVecteurAXDDGP")
    pspict.dilatation(1)

    fig.specific_needs="""\makeatletter\@ifundefined{vect}{\\newcommand{\\vect}[1]{\overrightarrow{#1}}}{}\makeatother"""

    v=(3,-1)
    A=Point(0,0)
    B=A+v
    C=A+(2,-3)
    D=C+v

    vect=AffineVector(A,B)
    vect.parameters.color="red"
    vect.put_mark(0.5,90,"\( \\vect{ AB }\)",pspict=pspict)

    d1=Segment(C,B)
    d1.parameters.color="blue"
    d1.parameters.style="dashed"

    M=d1.center()

    s1=Segment(A,M)
    s2=Segment(M,D)
    s1.parameters.color='brown'
    s2.parameters.color='brown'
    
    A.put_mark(0.3,90,"\( A\)",pspict=pspict)
    B.put_mark(0.2,-10,"\( B\)",pspict=pspict)
    C.put_mark(0.2,-90,"\( C\)",pspict=pspict)
    D.put_mark(0.2,0,"\( D\)",pspict=pspict)

    pspict.DrawGraphs(vect,d1,s1,s2,A,B,C,D,M)
    #pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
