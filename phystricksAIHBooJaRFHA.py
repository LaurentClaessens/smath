# -*- coding: utf8 -*-
from phystricks import *
def symmetric(seg,O):
    A=seg.I.symmetric_by(O)
    B=seg.F.symmetric_by(O)
    return Segment(A,B)

def AIHBooJaRFHA():
    pspict,fig = SinglePicture("AIHBooJaRFHA")
    pspict.dilatation(1)

    original=[]
    A=Point(0,0)
    original.append(  Segment(A,  A+(1,0) )  )
    original.append(  Segment(A,A+(0,-2))  )
    original.append(  Segment(A+(0,-0.5),A+(0.5,-0.5))  )

    O=Point(-1,-2.5)
    Op=Point(1.5,-2.5)

    prime=[  symmetric(seg,O) for seg in original ]
    pprime=[  symmetric(seg,Op) for seg in original ]

    for seg in prime :
        pspict.math_BB.append(seg)
    for seg in pprime :
        pspict.math_BB.append(seg)

    O.put_mark(0.2,180+45,"\( O\)",pspict=pspict,position="corner")
    Op.put_mark(0.2,-45,"\( O'\)",pspict=pspict,position="corner")
    
    pspict.DrawGraphs(original,O,Op)
    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
