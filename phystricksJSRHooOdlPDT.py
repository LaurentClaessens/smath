# -*- coding: utf8 -*-
from phystricks import *
def JSRHooOdlPDT():
    pspict,fig = SinglePicture("JSRHooOdlPDT")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    Mx=4.7
    mx=-5

    O=Point(0,0)
    A=Point(-3,0)
    B=Point(4,0)

    O.put_mark(0.2,-90,"\( O\)",automatic_place=(pspict,"N"))
    A.put_mark(0.2,-90,"\( -3\)",automatic_place=(pspict,"N"))
    A.put_mark(0.2,90+45,"\( A\)",automatic_place=(pspict,""))
    B.put_mark(0.2,-90,"\( 4\)",automatic_place=(pspict,""))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspict,""))

    mesA=Segment(O,A).get_measure(0.2,0.1,90,"\( 3\)",automatic_place=(pspict,"S"))
    mesB=Segment(O,B).get_measure(-0.2,0.1,90,"\( 4\)",automatic_place=(pspict,"S"))

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.no_numbering()

    pspict.DrawGraphs(axe,O,A,B,mesA,mesB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

