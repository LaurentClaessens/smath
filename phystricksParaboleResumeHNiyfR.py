# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def ParaboleResumeHNiyfR():
    pspict,fig = SinglePicture("ParaboleResumeHNiyfR")
    pspict.dilatation(1)

    x=var('x')
    x1=1
    x2=3
    f(x)=phyFunction((x-x1)*(x-x2)).graph(-1,4)
    s=(x1+x2)/2
    S=Point( s,f(s) )
    X0=Point(s,0)
    X1=Point(x1,0)
    X2=Point(x2,0)
    symetrie=Segment(Point(s,-3),Point(s,3))
    symetrie.parameters.color="red"
    X0.put_mark(0.2,90,"\( x_0\)",automatic_place=pspict)
    X1.put_mark(0.2,90,"\( x_1\)",automatic_place=pspict)
    X2.put_mark(0.2,90,"\( x_1\)",automatic_place=pspict)

    pspict.DrawGraphs(f,X1,X2,X0,S)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

