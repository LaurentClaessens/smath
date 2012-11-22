# -*- coding: utf8 -*-
from phystricks import *
def figureFNkqWFE():
    pspict,fig = SinglePicture("figureFNkqWFE")
    pspict.dilatation(1.5)

    v=(3,0)
    w=(1,2)
    A=Point(0,0)
    B=A+v
    C=B+w
    D=C-v

    paral=Polygon(A,B,C,D)
    A.put_mark(0.2,180,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,0,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,0,"\( C\)",automatic_place=pspict)
    D.put_mark(0.2,180,"\( D\)",automatic_place=pspict)

    d1=Segment(A,C)
    d2=Segment(D,B)
    d1.parameters.style="dashed"
    d2.parameters.style="dashed"
    O=Intersection(d1,d2)[0]
    O.put_mark(0.2,90,"\( O\)",automatic_place=pspict)


    AB=Segment(A,B)
    AB.put_mark(0.2,-90,"\( 4\sqrt{5}\)",automatic_place=pspict)
    AO=Segment(A,O)
    AO.put_mark(0.2,90,"\( 8\)",automatic_place=pspict)
    OB=Segment(O,B)
    OB.put_mark(0.2,45,"\( 4\)",automatic_place=pspict)

    pspict.DrawGraphs(paral,d1,d2,A,B,C,D,O,AB.mark,AO.mark,OB.mark)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
