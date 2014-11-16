# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def FLXBooMvWhiY():
    pspicts,figs = IndependentPictures("FLXBooMvWhiY",3)

    for psp in pspicts:
        psp.dilatation_X(0.3)
        psp.dilatation_Y(0.3)

    pspicts[2].dilatation_Y(0.1)

    x=var('x')
    absisses=[1,2,4,7]
    F=[   phyFunction(x/2),phyFunction(x/2+1),phyFunction(x**2-1)   ]

    pts=[   [Point(x,f(x)) for x in absisses  ] for f in F]

    for i,pt in enumerate(pts) :
        f=F[i].graph(absisses[0]-0.5,absisses[-1]+0.3)
        f.parameters.style="dashed"
        pspicts[i].DrawGraphs(pts[i],f)

    for psp in pspicts:
        psp.axes.no_graduation()
        psp.DrawDefaultAxes()

    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
