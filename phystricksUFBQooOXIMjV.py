# -*- coding: utf8 -*-
from phystricks import *
def UFBQooOXIMjV():
    pspicts,figs = IndependentPictures("UFBQooOXIMjV",2)

    for psp in pspicts:
        psp.dilatation(1)
    pspicts[0].rotation(30)
    pspicts[1].rotation(-15)

    l=7
    h=4
    A=Point(0,0)
    B=A+(0,h)
    C=B+(l,0)
    D=A+C-B
    rect=Polygon(A,B,C,D)
    rect.put_mark(0.4,pspict=pspicts)
    K=rect.edges[1].get_point_proportion(0.73)
    rect.edges[2].put_measure(measure_distance=-0.5,mark_distance=0.2,mark_angle=None,name="\( 4\)",automatic_place=(pspicts,""))

    trig1=Polygon(A,K,D)
    trig1.put_mark(0.4,points_names=" K ",pspict=pspicts)
    trig1.edges[2].put_measure(measure_distance=-0.5,mark_distance=0.2,mark_angle=None,name="\( 7\)",automatic_place=(pspicts,""))
    trig1.parameters.filled()
    trig1.parameters.fill.color="lightgray"

    L=rect.edges[3].get_point_proportion(0.3)
    trig2=Polygon(A,L,C)
    trig2.put_mark(0.4,points_names=" L ",pspict=pspicts)
    trig2.edges[0].put_measure(measure_distance=0.7,mark_distance=-0.7,mark_angle=None,name="\( 7\)",automatic_place=(pspicts,""))
    mLD=Segment(L,D).get_measure(measure_distance=0.7,mark_distance=-0.7,mark_angle=None,name="\( 3\)",automatic_place=(pspicts,""))
    trig2.parameters.filled()
    trig2.parameters.fill.color="lightgray"


    no_symbol(rect.vertices,trig1.vertices,trig2.vertices)
    pspicts[0].DrawGraphs(trig1)
    pspicts[1].DrawGraphs(trig2,mLD)
    for psp in pspicts:
        psp.comment="The whole is rotated"
        psp.DrawGraphs(rect)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

