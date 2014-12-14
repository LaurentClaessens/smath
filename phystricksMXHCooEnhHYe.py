# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def rect(a,b):
    return Polygon(  Point(a,0),Point(b,0),Point(b,1),Point(a,1)   )

def MXHCooEnhHYe():
    pspicts,figs = IndependentPictures("MXHCooEnhHYe",2)

    for psp in pspicts:
        psp.dilatation_X(4)
        psp.dilatation_Y(1/2)

    r1=rect(0,1/3)
    r2=rect(1/3,2/3)
    r3=rect(2/3,1)

    for re in [r1,r2]:
        re.parameters.filled()
        re.parameters.fill.color="lightgray"

    pspicts[0].DrawGraphs(r1,r2,r3)

    t=[   rect(  i/6,(i+1)/6  ) for i in range(0,6)    ]
    t[0].parameters.filled()
    t[0].parameters.fill.color="lightgray"
    pspicts[1].DrawGraphs(t)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
