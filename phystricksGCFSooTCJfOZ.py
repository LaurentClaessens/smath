# -*- coding: utf8 -*-
from phystricks import *
def GCFSooTCJfOZ():
    pspicts,figs = IndependentPictures("GCFSooTCJfOZ",2)
    for psp in pspicts :
        psp.dilatation(1)

    names_list=["A","B","C"]
    A=Point(0,0)
    B=Point(2,1)
    l=1
    K=Segment(A,B).orthogonal_trough(B).F
    v=K-B
    C=B+l*v

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,texts_list=[   "\( "+s+"\)" for s in names_list   ],pspict=pspicts)
    rh=RightAngle(Segment(A,B),Segment(B,C),0.2,1,1)
    pspict.DrawGraphs(trig,rh)
    names_list=["A","B","C"]

    names_list=["K","L","M"]
    A=Point(0,0)
    B=Point(1,3)
    l=-2
    K=Segment(A,B).orthogonal_trough(B)
    v=K-B
    C=B+l*v

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,texts_list=[   "\( "+s+"\)" for s in names_list   ],pspict=pspicts)
    rh=RightAngle(Segment(A,B),Segment(B,C),0.2,1,1)
    pspict.DrawGraphs(trig,rh)


    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
