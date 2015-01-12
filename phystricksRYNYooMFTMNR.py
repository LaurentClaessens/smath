# -*- coding: utf8 -*-
from phystricks import *
def RYNYooMFTMNR():
    pspicts,figs = IndependentPictures("RYNYooMFTMNR",2)
    for psp in pspicts :
        psp.dilatation(1)   

    v=(0,-1.5)
    A=Point(0,0)
    B=Point(6,0)
    C=A+v
    D=B+v

    s1=Segment(A,B)
    s2=Segment(C,D)

    angle=30*degree
    I=s2.get_point_proportion(0.2)
    directeur=(  cos(angle.radian),sin(angle.radian)  )
    support=Segment(I,I+directeur)
    J=Intersection(s1,support)[0]

    s3=Segment(I,J).dilatation(1.7)

    for psp in pspicts:
        psp.DrawGraphs(s1,s2,s3)

    a1=Angle(D,I,s3.F)
    a2=Angle(B,J,s3.F,0.5)
    pspicts[0].DrawGraphs(a1,a2)

    b1=a1
    b2=Angle(A,J,s3.I)
    pspicts[1].DrawGraphs(b1,b2)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
