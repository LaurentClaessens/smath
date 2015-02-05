# -*- coding: utf8 -*-
from phystricks import *
def GRBOooIZYhIV():
    pspict,fig = SinglePicture("GRBOooIZYhIV")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(1)

    mx=-4
    Mx=5

    K=Point(1,0)
    O=Point(0,0)
    A=Point(4,0)

    O.put_mark(0.2,-90,"\( 0\)",automatic_place=(pspict,""))
    A.put_mark(0.2,90,"\( A\)",automatic_place=(pspict,""))
    K.put_mark(0.2,90,"\(  K\)",automatic_place=(pspict,""))
    K.put_mark(0.2,-90,"\( 1\)",automatic_place=(pspict,""))

    for p in [O,K,A]:
        p.parameters.symbol=""

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.Dx=1
    axe.no_numbering()

    pspict.comment="Two marks on the point K : 'K' is written above and '1' is written under."
    pspict.DrawGraphs(axe,K,O,A)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
