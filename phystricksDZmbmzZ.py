# -*- coding: utf8 -*-
from phystricks import *
def DZmbmzZ():
    pspict,fig = SinglePicture("DZmbmzZ")
    pspict.dilatation(0.7)

    A=Point(3,4)
    B=Point(0,0)
    C=Point(6,0)

    BC=Segment(B,C)

    triangle=Polygon(A,B,C)
    A.put_mark(0.2,90,"\( A\)",pspict=pspict)
    B.put_mark(0.2,180,"\( B\)",pspict=pspict)
    C.put_mark(0.2,0,"\( C\)",pspict=pspict)

    H=A.projection(BC)
    H.put_mark(0.2,-90,"\( H\)",pspict=pspict)
    AH=Segment(A,H)
    AH.put_mark(0.2,0,"\( 4\)",pspict=pspict)

    a1=AngleAOB(B,A,H)
    a2=AngleAOB(H,A,C)
    a1.put_mark(text="\( 45\)",pspict=pspict)
    a2.put_mark(text="\( 60\)",pspict=pspict)

    pspict.DrawGraphs(triangle,A,B,C,AH,H,a1,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
