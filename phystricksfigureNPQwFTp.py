# -*- coding: utf8 -*-
from phystricks import *
def figureNPQwFTp():
    pspict,fig = SinglePicture("figureNPQwFTp")
    pspict.dilatation(1.2)

    A=Point(0,0)
    B=Point(4,0)
    C=Point(5,3)

    A.put_mark(0.2,180,"\( A\)",pspict=pspict)
    B.put_mark(0.2,0,"\( B\)",pspict=pspict)
    C.put_mark(0.2,90,"\( C\)",pspict=pspict)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CA=Segment(C,A)

    KA=BC.center()
    KA.put_mark(0.2,0,"\( I\)",pspict=pspict)
    hA=Segment(A,KA)
    KB=CA.center()
    KB.put_mark(0.2,135,"\( J\)",pspict=pspict)
    hB=Segment(B,KB)
    KC=AB.center()
    KC.put_mark(0.2,-90,"\( K\)",pspict=pspict)
    hC=Segment(C,KC)

    hA.parameters.color="red"
    hB.parameters.color="red"
    hC.parameters.color="red"

    G=Intersection(hA,hB)[0]
    G.put_mark(0.4,-90,"\( G\)",pspict=pspict)


    pspict.DrawGraphs(hA,hB,hC,AB,BC,CA,KA,KB,KC,G,A,B,C)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
