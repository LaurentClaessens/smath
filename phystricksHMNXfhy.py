# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def HMNXfhy():
    pspict,fig = SinglePicture("HMNXfhy")
    pspict.dilatation_X(0.2)
    pspict.dilatation_Y(0.2)

    a=6
    b=12

    A=Point(0,0)
    B=Point(a+b,0)
    C=Point(a+b,a+b)
    D=Point(0,a+b)

    pspict.DrawGraphs( Polygon( A,B,C,D  )  )
    pspict.DrawGraphs( Segment(Point(0,b/3),Point(b,b/3))  )    # Horizontale
    pspict.DrawGraphs( Segment( Point(b,0),Point(b,a+b) )   )   # verticale
    for i in [1,2]:
        pspict.DrawGraphs( Segment(Point(i*b/3,0),Point(i*b/3,b/3))  )
        pspict.DrawGraphs( Segment(Point(   b,i*a ),Point(a+b,i*a))  )
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
