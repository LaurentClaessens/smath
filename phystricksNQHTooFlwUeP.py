# -*- coding: utf8 -*-
from phystricks import *
def NQHTooFlwUeP():
    pspict,fig = SinglePicture("NQHTooFlwUeP")
    pspict.dilatation(1.5)

    x=var('x')
    curve1=ParametricCurve( 3*cos(x),3*sin(x) ).graph(0,2*pi-0.1)
    curve2=ParametricCurve( 2*cos(x),2*sin(x) ).graph(0,2*pi-0.1)
    curve1.parameters.color="red"
    curve2.parameters.color="red"

    surf=SurfaceBetweenParametricCurves(curve2,curve1,interval=(0,2*pi-0.1))
    surf.parameters.filled()
    surf.parameters.fill.color="blue"

    pspict.DrawGraphs(curve1,curve2,surf)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
