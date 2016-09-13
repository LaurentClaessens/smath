# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *

def LLBQooAjaorQ():
    pspicts,figs = IndependentPictures("LLBQooAjaorQ",2)
    for pspict in pspicts:
        pspict.dilatation(0.2)

    l=20
    h=13.5

    D=Point(0,0)
    A=D+(0,h)
    B=A+(l,0)
    C=D+(l,0)

    E=Point( h/(2*tan(35*2*pi/360)),h/2 )
    E.put_mark(0.2,angle=-45,text="\( E\)",pspicts=pspicts)
    F=Point(l,E.y)
    F.put_mark(0.2,angle=0,text="\( F\)",pspicts=pspicts)

    K=Intersection(   Segment(D,E),Segment(A,B)  )[0]
    K.put_mark(0.2,angle=90+45,text="\( K\)",pspicts=pspicts)
    EK=Segment(E,K)
    EK.parameters.style='dashed'

    bleu=Polygon(A,E,D)
    bleu.parameters.filled()
    bleu.parameters.fill.color="lightgray"
    rouge=Polygon(E,F,C,D)
    rouge.parameters.hatched()
    rouge.parameters.hatch.color="lightgray"

    drapeau=Polygon(A,B,C,D)
    drapeau.put_mark(0.2,pspicts=pspicts)

    no_symbol(A,B,C,D,E,K,F)

    pspicts[0].DrawGraphs(drapeau,E,bleu,rouge)
    pspicts[1].DrawGraphs(drapeau,E,bleu,rouge)
    pspicts[1].DrawGraphs(drapeau,E)

    tc=[]
    tc.append(AngleAOB(C,D,E))
    tc.append(AngleAOB(F,E,B))
    tc.append(AngleAOB(A,K,E))
    tc.append(AngleAOB(E,A,B))
    for ang in tc:
        ang.put_mark(0.3,angle=None,text="\SI{35}{\degree}",pspict=pspict)
    cc=[]
    cc.append(AngleAOB(E,D,A,r=0.3))
    cc.append(AngleAOB(D,A,E,r=0.3))
    for ang in cc:
        ang.put_mark(0.3,angle=None,text="\SI{55}{\degree}",pspict=pspict)
    cd=[]
    cd.append(AngleAOB(K,E,A,r=0.3))
    for ang in cd:
        ang.put_mark(0.3,angle=None,text="\SI{110}{\degree}",pspict=pspict)

    sep=AngleAOB(A,E,D,r=0.2)
    sep.put_mark(0.3,angle=None,text="\SI{70}{\degree}",pspict=pspict)

    pspicts[1].DrawGraphs(E,F,EK,tc,cc,cd,K,sep)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

