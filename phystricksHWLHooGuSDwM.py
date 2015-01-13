# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *

def symmetric(seg,O):
    A=seg.I.symmetric_by(O)
    B=seg.F.symmetric_by(O)
    return Segment(A,B)

def HWLHooGuSDwM():
    pspict,fig = SinglePicture("HWLHooGuSDwM")
    pspict.dilatation(0.5)
    
    l=3
    h=2
    A=Point(0,0)
    B=A+(l,0)
    C=B+(0,h)
    D=A+(0,h)
    S=(B+C)*0.5+(l/2,0)

    O=B+(3*l/2,0)
    O.put_mark(0.2,180,"\( O\)",automatic_place=(pspict,"E"))

    original=[]
    original.append( Segment(A,B)  )
    original.append( Segment(B,C)  )
    original.append( Segment(C,D)  )
    original.append( Segment(D,A)  )
    original.append( Segment(B,S)  )
    original.append( Segment(S,C)  )

    swip=[  symmetric(seg,O) for seg in original ]

    for s in swip:
        pspict.math_BB.append(s,pspict)
    for s in original:
        pspict.math_BB.append(s,pspict)

    pspict.DrawGraphs(original,O)
    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"
    pspict.comment="The grid is large enough to contain the picture and its image"
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
