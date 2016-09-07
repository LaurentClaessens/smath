# -*- coding: utf8 -*-
from phystricks import *

x=var('x')
f=LagrangePolynomial([Point(-1,-0),Point(0,0),Point(3,2),Point(6,-3)]).graph(-1.5,5.3)

def general(name):
    pspict,fig = SinglePicture(name)
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)
    f.put_mark(0.2,0,"\( f\)",pspict=pspict,position="W")

    pspict.DrawGraphs(f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    return pspict,fig

def PXsdjSu():
    pspict,fig=general("PXsdjSu")

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def LQGzkvL():
    pspict,fig=general("LQGzkvL")

    g=f.graph(-1.5,-0.5)
    g.wave(0.1,0.05)
    g.parameters.color="red"

    h=f.graph(3.2,5.3)
    h.wave(0.1,0.05)
    h.parameters.color="red"

    ante=f.inverse(2)
    pts=[  Point(x,f(x)) for x in ante if x>0 ]
    for i,P in enumerate(pts) :
        P.put_mark(0.2,90,"\( A_{{ {} }}\)".format(i+1),pspict=pspict,position="S")

    anteB=f.inverse(1)
    anteB=[x.real_part() for x in anteB]
    ptsB=[  Point(x,f(x)) for x in anteB if x>0  ]
    for i,P in enumerate(ptsB) :
        P.put_mark(0.2,90,"\( B_{{ {} }}\)".format(i+1),pspict=pspict,position="S")


    pspict.DrawGraphs(h,g,pts,ptsB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
