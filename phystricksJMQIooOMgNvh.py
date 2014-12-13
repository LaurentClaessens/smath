# -*- coding: utf8 -*-
from phystricks import *
def JMQIooOMgNvh():
    pspicts,figs = IndependentPictures("JMQIooOMgNvh",3)

    for psp in pspicts:
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.5)

    x=var('x')
    f1=phyFunction(x-4)
    f2=phyFunction(3*sqrt(x))
    f3=phyFunction(0.5*x)

    absisses=[1,2,4,7]
    F=[  f1,f2,f3   ]

    pts=[   [Point(x,f(x)) for x in absisses  ] for f in F]

    for i,pt in enumerate(pts) :
        f=F[i].graph(absisses[0]-0.5,absisses[-1]+0.3)
        f.parameters.style="dashed"
        pspicts[i].DrawGraphs(pts[i])

    for psp in pspicts:
        psp.axes.no_graduation()
        psp.DrawDefaultAxes()

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
