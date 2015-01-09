# -*- coding: utf8 -*-

from phystricks import *

def symmetric(seg,O):
    A=seg.I.symmetric_by(O)
    B=seg.F.symmetric_by(O)
    return Segment(A,B)

def SVPAooIuxHvP():
    pspict,fig = SinglePicture("SVPAooIuxHvP")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    original=[]
    A=Point(0,0)
    B=A+(1,0)
    C=A+(0,-2)
    D=C+B-A
    original.append(  Segment(A,  B)  )
    original.append(  Segment( B,C ))
    original.append(  Segment(C,D)  )

    O=Point(-1,-2.5)
    Op=Point(1.5,-2.5)

    prime=[  symmetric(seg,O) for seg in original ]
    pprime=[  symmetric(seg,Op) for seg in original ]

    for seg in prime :
        pspict.math_BB.append(seg)
    for seg in pprime :
        pspict.math_BB.append(seg)

    O.put_mark(0.2,180+45,"\( O\)",automatic_place=(pspict,"corner"))
    Op.put_mark(0.2,-45,"\( O'\)",automatic_place=(pspict,"corner"))
    
    pspict.DrawGraphs(original,O,Op)
    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
