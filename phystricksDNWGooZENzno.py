# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def DNWGooZENzno():
    pspict,fig = SinglePicture("DNWGooZENzno")
    pspict.dilatation(0.5)

    r=3
    A=Point(0,0)
    B=Point(r,0)
    C=Point(r,1)
    D=Point(0,1)
    cer=Circle(  Segment(D,C).midpoint(),r/2 ).graph(0,180)

    rect=Polygon(A,B,C,D)
    #rect.put_mark(0.2,pspict=pspict)

    surf=CustomSurface(  Segment(A,D),cer,Segment(C,B)  )
    surf.parameters.hatched()
    surf.parameters.hatch.color="lightgray"

    no_symbol(rect.vertices)
    pspict.DrawGraphs(surf,rect,cer)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

