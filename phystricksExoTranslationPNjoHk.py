# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def ExoTranslationPNjoHk():
    pspict,fig = SinglePicture("ExoTranslationPNjoHk")
    pspict.dilatation(0.7)

    pspict.specific_need="\\newcommand{\\vect}[1]{\overrightarrow{#1}}"

    l=2
    A=Point(1,1)
    B=A+(l,0)
    C=B+(0,l)
    D=A+(0,l)
    E=D+(l/2,1)

    Car=Polygon(A,B,C,D)
    Toit=Polygon(D,C,E)
    d1=Segment(D,B)
    d2=Segment(A,C)

    color="blue"
    Car.edges_parameters.color=color
    Toit.edges_parameters.color=color
    d1.parameters.color="blue"
    d2.parameters.color="blue"


    vA=Point(0,3)
    vB=vA+(1,2)
    v=AffineVector(vA,vB)
    v.parameters.color="red"
    vA.put_mark(0.2,270,"\( A\)",pspict=pspict)
    vB.put_mark(0.2,45,"\( B\)",pspict=pspict)
    vA.parameters.symbol=""
    vB.parameters.symbol=""

    pspict.DrawGraphs(Car,Toit,d1,d2,vA,vB,v)
    pspict.axes.no_numbering()
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    pspict.comment="The rectangle and triangle are drawn in blue."
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
