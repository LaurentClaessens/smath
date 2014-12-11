# -*- coding: utf8 -*-
from phystricks import *
def OBLUooWYQnuB():
    pspict,fig = SinglePicture("OBLUooWYQnuB")
    pspict.dilatation(1)

    l=4
    A=Point(0,0)
    B=A+(l,0)
    C=B+(0,l)
    D=A+(0,l)

    carre=Polygon(A,B,C,D)
    carre.put_mark(0.2,pspict=pspict)
    P=carre.edges[0].get_point_proportion(0.7)

    P.put_mark(0.2,45,"\( P\)",automatic_place=(pspict,"corner"))

    triangle=Polygon(A,P,D)
    triangle.parameters.filled()
    triangle.parameters.fill.color='lightgray'

    mesx=Segment(P,B).get_measure(0.2,0.1,-90,"\( x\)",automatic_place=(pspict,"N"))
    mesAP=Segment(A,P).get_measure(0.2,0.1,-90,"\(\\vphantom{H} \ldots\)",automatic_place=(pspict,"N"))
    mesAD=Segment(A,D).get_measure(-0.2,0.1,180,"\( \ldots\)",automatic_place=(pspict,"E"))

    pspict.DrawGraphs(carre,P,triangle,mesx,mesAP,mesAD)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

