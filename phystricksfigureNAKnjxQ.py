# -*- coding: utf8 -*-
from phystricks import *
def figureNAKnjxQ():
    pspict,fig = SinglePicture("figureNAKnjxQ")
    pspict.dilatation(1.2)

    A=Point(0,0)
    B=Point(4,0)
    C=Point(3,3)

    A.put_mark(0.2,180,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,0,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,90,"\( C\)",automatic_place=pspict)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CA=Segment(C,A)

    hA=BC.get_normal_vector().segment().dilatation(2.5)
    hB=CA.get_normal_vector().segment().dilatation(2)
    v=-AB.get_normal_vector()
    hC=v.segment().dilatation(2)

    hA.parameters.color="red"
    hB.parameters.color="red"
    hC.parameters.color="red"

    O=Intersection(hA,hB)[0]
    O.put_mark(0.4,-90,"\( \Omega\)",automatic_place=pspict)

    pspict.DrawGraphs(hA,hB,hC,AB,BC,CA,O,A,B,C)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
