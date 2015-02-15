# -*- coding: utf8 -*-
from phystricks import *
def figureWFDTzSN():
    pspict,fig = SinglePicture("figureWFDTzSN")
    pspict.dilatation(0.02)

    pspict.Mx_acceptable_BB=140

    O=Point(0,0)
    R=65
    h=56
    r=sqrt(R**2-h**2)
    cer=Circle(O,65)
    A=Point(-r,h)
    B=Point(r,h)
    C=Point(r,-h)
    D=Point(-r,-h)

    A.put_mark(0.2,135,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,-45,"\( C\)",automatic_place=pspict)
    D.put_mark(0.2,225,"\( D\)",automatic_place=pspict)
    O.put_mark(0.2,-90,"\( O\)",automatic_place=pspict)

    CB=Segment(C,B)
    hauteur=MeasureLength(CB,40)
    hauteur.put_mark(0.4,hauteur.advised_mark_angle(pspict),"\( 112\)",automatic_place=pspict)

    rect=Polygon(A,B,C,D)
    rect.edge.parameters.color="blue"

    pspict.DrawGraphs(cer,rect,A,B,C,D,O,hauteur)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
