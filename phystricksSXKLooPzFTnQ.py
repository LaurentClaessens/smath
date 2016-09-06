# -*- coding: utf8 -*-
from phystricks import *
def SXKLooPzFTnQ():
    pspict,fig = SinglePicture("SXKLooPzFTnQ")
    pspict.dilatation(1)


    O=Point(0,0)
    A=Point(-2,0)
    B=Point(2,0)
    C=Point(0,2)
    D=Point(0,-2)

    p1=Segment(A,B)
    p2=Segment(C,D)
    rh=RightAngleAOB(C,O,B)

    K=Circle(O,3).get_point(150)
    L=K.symmetric_by(O)

    a1=AngleAOB(C,O,K)
    a1.put_mark(0.4,angle=None,added_angle=0,text="\SI{50}{\degree}",pspict=pspict)
    a2=AngleAOB(D,O,L)
    a2.put_mark(0.4,angle=None,added_angle=0,text="?",pspict=pspict)

    seg=Segment(K,L)

    pspict.DrawGraphs(p1,p2,rh,seg,a1,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
