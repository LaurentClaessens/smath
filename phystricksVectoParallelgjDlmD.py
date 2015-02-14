# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

from phystricksVectoParallItzteT import situation

def VectoParallelgjDlmD():
    pspict,fig = SinglePicture("VectoParallelgjDlmD")
    pspict.dilatation(2)

    graphes = situation(pspict)

    #parABDC,parABKpK,seg1,seg2,
    AB=graphes[4]
    A=graphes[5]
    B=graphes[6]
    C=graphes[7]
    D=graphes[8]
    K=graphes[9]
    Kp=graphes[10]

    ABp=AB.dilatation(1.7)

    I=ABp.I
    F=ABp.F

    a1=Angle(I,A,K)
    a2=Angle(A,B,Kp)
    a2.r=a2.r+0.1
    a1.r=a2.r
    a1.put_mark(0.2,None,"\( \\alpha\)",automatic_place=pspict)
    a2.put_mark(0.2,None,"\( \\alpha\)",automatic_place=pspict)
    a1.parameters.color="green"
    a2.parameters.color="green"

    b1=Angle(C,A,B)
    b2=Angle(D,B,F)
    b1.r=b2.r
    b1.put_mark(0.2,None,"\( \\beta\)",automatic_place=pspict)
    b2.put_mark(0.2,None,"\( \\beta\)",automatic_place=pspict)
    b1.parameters.color="cyan"
    b2.parameters.color="cyan"

    c1=Angle(K,A,C)
    c2=Angle(Kp,B,D)
    c1.r=c2.r
    c1.put_mark(0.2,None,"\( \hat A\)",automatic_place=pspict)
    c2.put_mark(0.2,None,"\( \hat B\)",automatic_place=pspict)
    c1.parameters.color="brown"
    c2.parameters.color="brown"


    pspict.DrawGraphs(ABp,graphes,a1,a2,b1,b2,c1,c2)
    fig.conclude()
    fig.write_the_file()
