# -*- coding: utf8 -*-
from phystricks import *
def DefVecteurAXDDGP():
    pspict,fig = SinglePicture("DefVecteurAXDDGP")
    pspict.dilatation(1)

    pspict.specific_needs="\\newcommand{\\vect}[1]{\overrightarrow{#1}}"

    v=(3,-1)
    A=Point(0,0)
    B=A+v
    C=A+(2,-3)
    D=C+v

    vect=AffineVector(A,B)
    vect.parameters.color="red"
    vect.put_mark(0.5,90,"\( \\vect{ AB }\)",automatic_place=pspict)

    d1=Segment(C,B)
    d1.parameters.color="blue"
    d1.parameters.style="dashed"

    M=d1.center()

    s1=Segment(A,M)
    s2=Segment(M,D)
    s1.parameters.color='brown'
    s2.parameters.color='brown'
    
    A.put_mark(0.3,90,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,-10,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,-90,"\( C\)",automatic_place=pspict)
    D.put_mark(0.2,0,"\( D\)",automatic_place=pspict)

    pspict.DrawGraphs(A,B,C,D,M,vect,d1,s1,s2)
    #pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
