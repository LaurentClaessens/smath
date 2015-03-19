# -*- coding: utf8 -*-
from phystricks import *
def HRIVooBXxZES():
    pspict,fig = SinglePicture("HRIVooBXxZES")
    pspict.dilatation_X(5)
    pspict.dilatation_Y(3)

    A=Point(0,0)
    B=A+(-1,-2)
    C=A+(1,-2)
    D=A+(-1,0)

    trig=Polygon(A,B,C)
    trig.put_mark(0.4,pspict=pspict)
    D.put_mark(0.2,angle=180,text="\( D\)",automatic_place=(pspict,""))

    droite=Segment(D,B).dilatation(1.5)

    a1=Angle(B,A,C)
    a2=Angle(C,B,A,r=0.7)
    a3=Angle(A,B,D,r=0.5)

    a1.put_mark(0.2,angle=None,text="\SI{40}{\degree}",automatic_place=(pspict,""))
    a2.put_mark(0.2,angle=None,text="?",automatic_place=(pspict,""))
    a3.put_mark(0.2,angle=None,text="?",automatic_place=(pspict,""))

    trig.edges[0].put_code(n=2,d=0.1,l=0.1,pspict=pspict)
    trig.edges[2].put_code(n=2,d=0.1,l=0.1,pspict=pspict)

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,D,droite,a1,a2,a3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
