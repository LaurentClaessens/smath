# -*- coding: utf8 -*-
from phystricks import *
def IDKXooPrOOeE():
    pspict,fig = SinglePicture("IDKXooPrOOeE")

    pspict.dilatation(1)

    l=5
    h=4
    perspective=ObliqueProjection(30,0.5)
    A=perspective.point(0,0,0)
    B=perspective.point(l,0,0)
    C=perspective.point(l,0,l)
    D=perspective.point(0,0,l)
    a=2*l/3-0.2
    b=l/3
    S=perspective.point(a,h,b)
    I=perspective.point(a,0,b)

    hauteur=Segment(S,I)
    minidig=Segment(B,I)
    hauteur.parameters.style="dotted"
    minidig.parameters.style="dashed"

    for pt in [A,B,C,D]:
        pt=pt.rotation(30)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CS=Segment(C,S)
    AS=Segment(A,S)
    BS=Segment(B,S)

    AB.put_mark(0.2,angle=-90,text="\( 4\)",automatic_place=(pspict,""))
    BC.put_mark(0.2,angle=None,text="\( 3\)",added_angle=180,automatic_place=(pspict,""))
    hauteur.put_mark(0.2,angle=0,text="\( 6\)",automatic_place=(pspict,""))

    AD=Segment(A,D)
    AD.parameters.style='dashed'
    DC=Segment(D,C)
    DC.parameters.style='dashed'
    SD=Segment(S,D)
    SD.parameters.style='dashed'

    A.put_mark(0.2,180+45,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,-45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,45,"\( C\)",automatic_place=pspict)
    D.put_mark(0.1,90+45,"\( D\)",automatic_place=pspict)
    S.put_mark(0.2,90,"\( S\)",automatic_place=pspict)
    I.put_mark(0.2,angle=90+45,text="\( I\)",automatic_place=(pspict,""))

    rh=RightAngle( Segment(S,I),Segment(I,B),0.3,0,1 )
    rhA=RightAngle( Segment(A,B),Segment(A,D),0.3,1,1 )
    rhC=RightAngle( Segment(D,C),Segment(C,B),0.3,0,1 )


    no_symbol(A,B,C,D,S)
    
    pspict.DrawGraphs(A,B,C,D,S,BS,AB,BC,CS,AS,AD,DC,SD,hauteur,minidig,I,rh,rhA,rhC)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
