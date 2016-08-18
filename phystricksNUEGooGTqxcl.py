# -*- coding: utf8 -*-
from phystricks import *

def symmetric(seg,O):
    A=seg.I.symmetric_by(O)
    B=seg.F.symmetric_by(O)
    return Segment(A,B)

def axial(seg):
    A=Point(  seg.I.x,-seg.I.y  )
    B=Point(  seg.F.x,-seg.F.y  )
    return Segment(A,B)

def NUEGooGTqxcl():
    pspict,fig = SinglePicture("NUEGooGTqxcl")
    pspict.dilatation(0.5)

    A=Point(3,4)
    B=Point(5,2)
    C=Point(7,4)
    D=Point(5,6)
    E=Point(7,6)
    O=Point(3,0)
    O.put_mark(0.2,45,"\( O\)",pspict=pspict)

    maison=[   Segment(A,B),Segment(B,C),Segment(C,D),Segment(D,E),Segment(E,C),Segment(A,D)  ]
    maison1=[  symmetric(s,O) for s in maison  ]
    maison2=[  axial(s) for s in maison  ]

    for s in maison1:
        s.parameters.color="red"
    for s in maison2:
        s.parameters.color="blue"

    pspict.DrawGraphs(maison,maison1,maison2,O)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
