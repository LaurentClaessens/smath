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

    P.put_mark(0.1,45,"\( P\)",pspict=pspict,position="corner")

    triangle=Polygon(A,P,D)
    triangle.filled()
    triangle.fill_parameters.color='lightgray'

    mesx=Segment(P,B).get_measure(0.2,0.1,text="\( \ell\)",pspict=pspict,position="N")
    mesAP=Segment(A,P).get_measure(0.2,0.1,text="\(\\vphantom{H} \ldots\)",pspict=pspict,position="N")
    mesAD=Segment(A,D).get_measure(-0.2,0.1,text="\( \ldots\)",pspict=pspict,position="E")

    for s in [A,B,C,D,P]:
        s.parameters.symbol=""

    pspict.DrawGraphs(carre,P,triangle,mesx,mesAP,mesAD)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
