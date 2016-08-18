# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def symmetric(seg,O):
    A=seg.I.symmetric_by(O)
    B=seg.F.symmetric_by(O)
    return Segment(A,B)

def RGRLooTmnwQZ():
    pspict,fig = SinglePicture("RGRLooTmnwQZ")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    d=1
    h=3
    s=0.5
    
    A=Point(0,0)

    original=[]
    # T
    original.append( Segment( A+(-d,0),A+(d,0) ) )
    original.append( Segment(A,A+(0,-h)))
    # E
    B=A+(d,0)+(s,0)
    original.append( Segment(B,B+(d,0))    )
    original.append( Segment(B,B+(0,-h))  )
    C=B+(0,-h/2)
    original.append( Segment(C,C+(d,0))  )
    original.append( Segment(  B+(0,-h)  ,B+(d,-h))  )
    #original.append( Segment(<++>,<++>)  )
    #original.append( Segment(<++>,<++>)  )
    # X
    D=B+(d+s,0)
    original.append( Segment(D,D+(2*d,-h))  )
    original.append( Segment(D+(0,-h),D+(2*d,0))  )

    O=A+(2*d+s,-3*h/2)
    O.put_mark(0.2,180,"\( O\)",pspict=pspict,position="E")
    swip=[  symmetric(seg,O) for seg in original ]


    choix=[]
    import random
    for i in range(len(original)):
        choix.append(  random.choice(  [original[i],swip[i]]  )   )

    for s in swip:
        pspict.math_BB.append(s,pspict)
    for s in original:
        pspict.math_BB.append(s,pspict)

    #for seg in choix:
    #    seg.parameters.color="blue"


    pspict.comment="The grid is large enough to contain the image"
    pspict.DrawGraphs(choix,O)
    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"
    pspict.comment="The grid is dotted"
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

