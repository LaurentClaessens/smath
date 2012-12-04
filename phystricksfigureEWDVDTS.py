# -*- coding: utf8 -*-
from phystricks import *
def figureEWDVDTS():
    pspict,fig = SinglePicture("figureEWDVDTS")
    pspict.dilatation(1)

    x=var('x')
    l=2.8
    f=phyFunction(x**2).graph(-l,l)
        
    pspict.DrawGraphs(f)

    a=2
    for k in [a,-a]:
        A=f.get_point(k)
        Ap=Point(A.x,0)
        s=Segment(A,Ap)
        s.parameters.style="dashed"
        pspict.DrawGraphs(A,Ap,s)

    h=f(a)
    horiz=Segment(Point(-l,h),Point(l,h))
    soluce=Segment(Point(-a,0),Point(a,0))
    soluce.wave(0.2,0.1)
    soluce.parameters.color="cyan"

    pspict.DrawGraphs(horiz,soluce)

    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
