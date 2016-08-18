# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def ParaboleResumeHNiyfR():
    pspict,fig = SinglePicture("ParaboleResumeHNiyfR")
    pspict.dilatation(1)

    x=var('x')
    mx=-0.5
    Mx=5.5
    x1=1
    x2=4
    f=phyFunction((x-x1)*(x-x2)/2).graph(mx,Mx)
    s=(x1+x2)/2
    S=Point( s,f(s) )
    X0=Point(s,0)
    X1=Point(x1,0)
    X2=Point(x2,0)
    symetrie=Segment(Point(s,f(s)-1),Point(s,f(Mx)+0.5))
    symetrie.parameters.color="red"
    X0.put_mark(0.2,45,"\( x_0\)",pspict=pspict)
    X1.put_mark(0.2,225,"\( x_1\)",pspict=pspict)
    X2.put_mark(0.2,-45,"\( x_2\)",pspict=pspict)
    S.put_mark(0.2,-45,"\( S\)",pspict=pspict)

    pspict.DrawGraphs(f,symetrie,X1,X2,X0,S)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

