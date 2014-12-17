# -*- coding: utf8 -*-
from phystricks import *
def CZFJooUDaKCj():
    pspict,fig = SinglePicture("CZFJooUDaKCj")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(1)

    mx=0
    Mx=10
    O=Point(0,0)

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.no_numbering()
    
    pspict.DrawGraphs(axe)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
