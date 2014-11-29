# -*- coding: utf8 -*-
from phystricks import *
def CFWIooWDSwRD():
    pspict,fig = SinglePicture("CFWIooWDSwRD")
    pspict.dilatation(0.5)

    O=Point(0,0)
    rayons=[3,4,5,6,7]
    cercles=[  Circle(O,r).graph(0,2*pi*radian) for r in rayons  ]

    c1=cercles[0]
    c2=cercles[1]

    couronne=SurfaceBetweenParametricCurves(c1,c2)
    couronne.parameters.filled()
    couronne.parameters.fill.color="red"

    c1.parameters.color="blue"
    c2.parameters.color="cyan"

    pspict.DrawGraphs(cercles,couronne,c1,c2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
