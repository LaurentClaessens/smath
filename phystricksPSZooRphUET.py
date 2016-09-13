# -*- coding: utf8 -*-
from phystricks import *
def PSZooRphUET():
    pspict,fig = SinglePicture("PSZooRphUET")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    K=Point(0,0)
    L=Point(10,0)
    c1=Circle(K,6).graph(20,45)
    c2=Circle(L,6).graph(90+45,180-20)

    c1.parameters.style="dashed"
    c2.parameters.style="dashed"

    M=Intersection(c1,c2)[1]

    K.put_mark(0.2,180+45,"\( K\)",pspict=pspict,position="corner")
    L.put_mark(0.2,-45,"\( L\)",pspict=pspict,position="corner")
    M.put_mark(0.2,text="\( M\)",pspict=pspict,position="S")

    trig=Polygon(K,L,M)

    a1=AngleAOB(L,K,M)
    a2=AngleAOB(M,L,K)
    a3=AngleAOB(K,M,L)
    a1.put_mark(0.4,None,"\SI{33}{\degree}",pspict=pspict)
    a2.put_mark(0.4,None,"\SI{33}{\degree}",pspict=pspict)
    a3.put_mark(0.4,None,"\SI{113}{\degree}",pspict=pspict)

    pspict.DrawGraphs(K,L,M,c1,c2,trig,a1,a2,a3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
