# -*- coding: utf8 -*-
from phystricks import *
def NWPooWQBSnz():
    pspict,fig = SinglePicture("NWPooWQBSnz")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    A=Point(4,2)
    B=Point(0,0)
    C=Point(5,0)
    H=Point(A.x,0)

    C1=Circle(  Segment(B,A).midpoint(),0.3 )
    C1.parameters.filled()
    C1.parameters.fill.color='white'

    C2=Circle(  Segment(C,A).midpoint(),0.3 )
    C2.parameters.filled()
    C2.parameters.fill.color='white'

    triangle=Polygon(A,B,C)
    A.put_mark(0.2,text="\( A\)",pspict=pspict,position="S")
    B.put_mark(0.2,180+45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict,position="corner")
    H.put_mark(0.2,text="\( H\)",pspict=pspict,position="N")

    hauteur=Segment(A,H)
    hauteur.parameters.style="dashed"

    rh=RightAngleAOB(A,H,B)

    no_symbol(A,B,C,H)
    pspict.DrawGraphs(triangle,A,B,C,H,hauteur,C1,C2,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
