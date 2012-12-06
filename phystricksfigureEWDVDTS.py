# -*- coding: utf8 -*-
from phystricks import *
def figureEWDVDTS():
    pspict,fig = SinglePicture("figureEWDVDTS")
    pspict.dilatation(1)

    x=var('x')
    l=2.8
    f=phyFunction(x**2).graph(-l,l)
        
    pspict.DrawGraphs(f)

    a=2     # Ce 2 est hard-codé dans le texte. (x^2\leq 4)

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

    soluceg1=Segment(Point(-l,0),Point(-a,0))
    soluceg2=Segment(Point(a,0),Point(l,0))
    soluceg1.wave(0.2,0.1)
    soluceg2.wave(0.2,0.1)
    soluceg1.parameters.color="red"
    soluceg2.parameters.color="red"

    pspict.DrawGraphs(horiz,soluce,soluceg1,soluceg2)

    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
