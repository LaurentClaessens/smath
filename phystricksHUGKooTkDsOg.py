# -*- coding: utf8 -*-
from phystricks import *
def HUGKooTkDsOg():
    pspict,fig = SinglePicture("HUGKooTkDsOg")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(2,3)
    C=B+(4,-4)
    D=A+C-B

    parall=Polygon(A,B,C,D)
    parall.put_mark(0.3,pspict=pspict)

    diag=Segment(parall.vertices[0],parall.vertices[2])
    a1=AngleAOB(B,C,A,r=0.8)
    a1.put_mark(0.8,angle=None,added_angle=0,text="\SI{30}{\degree}",pspict=pspict)

    #a5=AngleAOB(B,C,A,r=0.8)
    #a5.put_mark(0.8,angle=None,added_angle=0,text="\SI{30}{\degree}",pspict=pspict)

    a2=AngleAOB(D,A,C,r=0.8)
    a2.put_mark(0.4,angle=None,added_angle=0,text="?",pspict=pspict)
    a3=AngleAOB(C,D,A)
    a3.put_mark(0.4,angle=None,added_angle=0,text="\SI{80}{\degree}",pspict=pspict)
    a4=AngleAOB(A,B,C)
    a4.put_mark(0.4,angle=None,added_angle=0,text="?",pspict=pspict)

    no_symbol(parall.vertices)
    pspict.DrawGraphs(parall,diag,a1,a2,a3,a4)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
