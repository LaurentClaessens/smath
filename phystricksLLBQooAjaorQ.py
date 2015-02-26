# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *

def LLBQooAjaorQ():
    pspict,fig = SinglePicture("LLBQooAjaorQ")
    pspict.dilatation(0.3)

    l=20
    h=13.5

    D=Point(0,0)
    A=D+(0,h)
    B=A+(l,0)
    C=D+(l,0)

    E=Point( h/(2*tan(35*2*pi/360)),h/2 )
    E.put_mark(0.2,angle=45,text="\( E\)",automatic_place=(pspict,""))
    F=Point(l,E.y)

    bleu=Polygon(A,E,D)
    bleu.parameters.filled()
    bleu.parameters.fill.color="lightgray"
    rouge=Polygon(E,F,C,D)
    rouge.parameters.hatched()
    rouge.parameters.hatch.color="lightgray"

    drapeau=Polygon(A,B,C,D)
    drapeau.put_mark(0.2,pspict=pspict)

    no_symbol(A,B,C,D,E)

    pspict.DrawGraphs(drapeau,E,bleu,rouge)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

