# -*- coding: utf8 -*-
from phystricks import *

def mathize(text):
    return "$"+text+"$"

def ELFXooRwIoJO():
    pspict,fig = SinglePicture("ELFXooRwIoJO")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    K=Point(0,0)
    M=Point(10,0)
    L=Point(M.x,6)

    A=Point(1,0)
    B=Point(4,0)
    C=Point(L.x-1,0)

    trig=Polygon(K,L,M)
    trig.put_mark(0.4,points_names="KLM",pspict=pspict)

    for ba in [(A,"A"),(B,"B"),(C,"C")]:
        pt=ba[0]
        nom=ba[1]
        ptp=trig.edges[0].get_point(pt.x)
        pt.put_mark(0.2,angle=-90,added_angle=0,text=mathize(nom),pspict=pspict)
        ptp.put_mark(0.2,angle=90,added_angle=0,text=mathize(nom+"'"),pspict=pspict)
        seg=Segment(pt,ptp)
        pspict.DrawGraphs(seg,pt,ptp)
        no_symbol(pt,ptp)

    no_symbol(trig.vertices,A,B,C)
    pspict.DrawGraphs(A,B,C,trig)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
