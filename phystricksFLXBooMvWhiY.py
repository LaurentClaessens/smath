# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def FLXBooMvWhiY():
    pspicts,figs = IndependentPictures("FLXBooMvWhiY",3)

    for psp in pspicts:
        psp.dilatation_X(0.5)
        psp.dilatation_Y(1)

    pspicts[2].dilatation_Y(0.1)

    pts=[   [Point(x,x/2) for x in [1,2,4,7]], [Point(x,x/2+1) for x in [1,2,4,7]], [Point(x,x**2-1) for x in [1,2,4,7]]  ]

    for i in range(len(pts)):
        pspicts[i].DrawGraphs(pts[i])

    for psp in pspicts:
        psp.axes.no_graduation()
        psp.DrawDefaultAxes()

    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
