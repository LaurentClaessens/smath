# -*- coding: utf8 -*-
from phystricks import *
def XUBNooNxZEmS():
    pspict,fig = SinglePicture("XUBNooNxZEmS")
    pspict.dilatation(0.56)

    L=10
    l=7
    h=3
    A=Point(0,0)
    B=A+(l,0)
    C=A+(L,0)
    D=C+(0,h)
    E=B+(0,h)
    F=A+(0,h)

    jardin=Polygon(A,B,E,F)
    piscine=Polygon(B,C,D,E)
    piscine.hatched()
    piscine.hatch_parameters.color="lightgray"

    mesL=Segment(F,D).get_measure(-0.2,0.1,text="\( 10\)",pspict=pspict,position="S")
    mesl=Segment(A,B).get_measure(0.2,0.1,text="\( 6\)",pspict=pspict,position="N")
    mesH=Segment(A,F).get_measure(-0.2,0.1,text="\( 3\)",pspict=pspict,position="E")

    pspict.DrawGraphs(piscine,jardin,mesL,mesl,mesH)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
