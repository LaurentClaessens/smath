# -*- coding: utf8 -*-
from phystricks import *
def UFBQooOXIMjV():
    pspicts,figs = IndependentPictures("UFBQooOXIMjV",2)

    for psp in pspicts:
        psp.dilatation(1)
    pspicts[0].rotation=30
    pspicts[1].rotation=73

    l=7
    h=4
    A=Point(0,0)
    B=A+(0,h)
    C=B+(l,0)
    D=A+C-B
    rect=Polygon(A,B,C,D)
    rect.put_mark(0.4,pspict=pspicts)
    K=rect.edges[1].get_point_proportion(0.73)
    trig=Polygon(A,K,D)
    trig.put_mark(0.4,points_names=" K ",pspict=pspicts)

    trig.edges[2].put_measure(-0.3,0.2,0,"7",automatic_place=(pspicts,""))
    rect.edges[2].put_measure(-0.3,0.2,0,"4",automatic_place=(pspicts,""))

    no_symbol(rect.vertices,trig.vertices)
    for psp in pspicts:
        psp.DrawGraphs(rect,trig)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

