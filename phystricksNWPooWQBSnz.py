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

    C1=Circle(  Segment(B,A).center(),0.3 )
    C1.parameters.filled()
    C1.parameters.fill.color='white'

    C2=Circle(  Segment(C,A).center(),0.3 )
    C2.parameters.filled()
    C2.parameters.fill.color='white'

    triangle=Polygon(A,B,C)
    A.put_mark(0.2,90,"\( A\)",automatic_place=(pspict,"S"))
    B.put_mark(0.2,180+45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-45,"\( C\)",automatic_place=(pspict,"corner"))
    H.put_mark(0.2,-90,"\( H\)",automatic_place=(pspict,"N"))

    hauteur=Segment(A,H)
    hauteur.parameters.style="dashed"

    rh=RightAngleAOB(A,H,B)

    no_symbol(A,B,C,H)
    pspict.DrawGraphs(triangle,A,B,C,H,hauteur,C1,C2,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
