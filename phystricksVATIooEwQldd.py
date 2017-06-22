# -*- coding: utf8 -*-
from phystricks import *
def VATIooEwQldd():
    pspicts,figs = IndependentPictures("VATIooEwQldd",2)

    for psp in pspicts:
        psp.dilatation(0.7)
    pspicts[0].rotation(45)
    pspicts[1].rotation(-20)

    l=7
    h=4
    A=Point(0,0)
    B=A+(0,h)
    C=B+(l,0)
    D=A+C-B
    rect=Polygon(A,B,C,D)
    rect.put_mark(0.4,pspicts=pspicts)
    K=rect.edges[1].get_point_proportion(0.73)
    rect.edges[2].put_measure(measure_distance=-0.5,mark_distance=0.2,mark_angle=None,text="\SI{3}{\centi\meter}",pspicts=pspicts)

    trig1=Polygon(A,K,D)
    trig1.put_mark(0.4,points_names=" K ",pspicts=pspicts)
    trig1.edges[2].put_measure(measure_distance=-0.5,mark_distance=0.2,mark_angle=None,text="\SI{7}{\centi\meter}",pspicts=pspicts)
    trig1.filled()
    trig1.fill_parameters.color="lightgray"

    M=rect.edges[3].get_point_proportion(0.3)
    trig2=Polygon(B,C,M)
    M.put_mark(0.2,angle=None,added_angle=0,text="\( M\)",pspicts=pspicts)
    trig2.edges[0].put_measure(measure_distance=-0.5,mark_distance=0.2,mark_angle=None,text="\SI{5}{\centi\meter}",pspicts=pspicts)
    trig2.filled()
    trig2.fill_parameters.color="lightgray"


    no_symbol(rect.vertices,trig1.vertices,trig2.vertices)
    pspicts[0].DrawGraphs(trig1)
    pspicts[1].DrawGraphs(trig2,M)
    for psp in pspicts:
        psp.comment="The whole is rotated"
        psp.DrawGraphs(rect)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
