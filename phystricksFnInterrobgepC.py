# -*- coding: utf8 -*-
from phystricks import *
def FnInterrobgepC():
    pspict,fig = SinglePicture("FnInterrobgepC")
    pspict.dilatation(0.7)

    x=var('x')
    f=LagrangePolynomial([Point(-3,1),Point(0,0),Point(3,7),Point(5,-1)]).graph(-3.5,5.5)
    f.put_mark(0.2,0,"\( f\)",pspict=pspict)
    g=LagrangePolynomial([Point(1,3),Point(4,5),Point(-1,1)]).graph(-3.5,5.5)
    g.put_mark(0.2,0,"\( g\)",pspict=pspict)
    g.parameters.style="dashed"

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

