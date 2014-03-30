# -*- coding: utf8 -*-
from phystricks import *
def VGQoojvDGr():
    pspict,fig = SinglePicture("VGQoojvDGr")
    pspict.dilatation_X(0.6)
    pspict.dilatation_Y(1)

    O=Point(0,0)
    I=Point(1,0)
    A=Point(3,0)
    B=Point(4,0)
    C=Point(7,0)
    K=Point(-1,0)
    L=Point(-5,0)

    A.put_mark(0.2,-90,"\( A\)",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-90,"\( B\)",automatic_place=(pspict,"N"))
    C.put_mark(0.2,-90,"\( C\)",automatic_place=(pspict,"N"))
    K.put_mark(0.2,-90,"\( K\)",automatic_place=(pspict,"N"))
    L.put_mark(0.2,-90,"\( L\)",automatic_place=(pspict,"N"))
    O.put_mark(0.2,-90,"\( O\)",automatic_place=(pspict,"N"))
    I.put_mark(0.2,-90,"\( I\)",automatic_place=(pspict,"N"))

    pspict.DrawGraphs(A,B,C,K,L,O,I)

    pspict.axes.no_numbering()
    pspict.axes.draw_single_axeY=False
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
