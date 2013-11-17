# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def FWyrYhJ():
    pspict,fig = SinglePicture("FWyrYhJ")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(5)

    E=[3,0,1,4,4,2,1,5,3,1,1]
    tot=sum(E)
    ECC=0
    for i,k in enumerate(E):
        ECC=ECC+k
        y=ECC/tot
        P=Point(i+1,y)
        pspict.DrawGraphs(P)

    pspict.axes.single_axeY.Dx=0.25
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
