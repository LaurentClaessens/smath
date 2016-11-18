# -*- coding: utf8 -*-
from phystricks import *
def SWFywZG():
    pspict,fig = SinglePicture("SWFywZG")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(1,2)
    K=Point(-3,3)
    S=Point(0,5)
    L=Point(7,1)

    A.put_mark(0.2,45,"\( A\)",pspict=pspict,position="corner")
    K.put_mark(0.2,text="\( K\)",pspict=pspict,position="S")

    s1=Segment(K,S)
    s2=Segment(S,A)
    s3=Segment(A,L)

    pspict.DrawGraphs(A,K,s1,s2,s3)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
