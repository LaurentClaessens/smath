# -*- coding: utf8 -*-
from phystricks import *
def DSBHooZdaNyy():
    pspict,fig = SinglePicture("DSBHooZdaNyy")
    pspict.dilatation_X(0.56)
    pspict.dilatation_Y(0.33)
    
    L=10
    l=4
    h=3
    A=Point(0,0)
    B=A+(l,0)
    C=A+(L,0)
    D=C+(0,h)
    E=B+(0,h)
    F=A+(0,h)

    jardin=Polygon(A,B,E,F)
    piscine=Polygon(B,C,D,E)
    piscine.parameters.hatched()
    piscine.parameters.hatch.color="lightgray"

    mesL=Segment(F,D).get_measure(-0.3,0.1,90,"\( 10\)",automatic_place=(pspict,"S"))
    mesl=Segment(A,B).get_measure(0.3,0.1,-90,"\( x\)",automatic_place=(pspict,"N"))
    mesH=Segment(A,F).get_measure(-0.3,0.1,180,"\( 3\)",automatic_place=(pspict,"E"))
    #mesP=Segment(B,C).get_measure(0.2,0.1,-90,"\( 10-x\)",automatic_place=(pspict,"N"))

    pspict.DrawGraphs(piscine,jardin,mesL,mesl,mesH)
    #pspict.DrawGraphs(piscine,jardin,mesL,mesl,mesH,mesP)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
