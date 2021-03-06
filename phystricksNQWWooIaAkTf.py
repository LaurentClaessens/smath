# -*- coding: utf8 -*-
from phystricks import *
def NQWWooIaAkTf():
    pspict,fig = SinglePicture("NQWWooIaAkTf")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    L=4
    pr1=0.34
    pr2=0.8
    O=Point(0,0)
    P=Point(L,0)
    Q=Point(0.5,L)
    A=Segment(O,Q).get_point_proportion(pr2)
    B=Segment(O,P).get_point_proportion(pr2)
    C=Segment(O,P).get_point_proportion(pr1)
    D=Segment(O,Q).get_point_proportion(pr1)
    s1=Segment(O,P)
    s2=Segment(O,Q)
    p1=Segment(D,C).dilatation(1.3)
    p2=Segment(A,B).dilatation(1.3)

    O.put_mark(0.2,angle=180+45,text="\( O\)",pspict=pspict)
    #A.put_mark(0.2,angle=45,text="\( A\)",pspict=pspict)
    #mA=AngleAOB(p2.I,A,O,r=0.1).get_mark(0.2,None,text="\( A\)",pspict=pspict)
    mA=AngleAOB(B,A,Q,r=0.1).get_mark(0.2,None,text="\( A\)",pspict=pspict)


    B.put_mark(0.2,angle=45,text="\( B\)",pspict=pspict)
    C.put_mark(0.2,angle=180+45,text="\( C\)",pspict=pspict)
    D.put_mark(0.2,angle=180+45,text="\( D\)",pspict=pspict)

    m1=Segment(D,C).get_mark(0.1,angle=None,text="\( 3\)",pspict=pspict)
    m2=Segment(A,B).get_mark(0.1,angle=None,text="\( 7\)",pspict=pspict)

    no_symbol(B,C,D,O)

    pspict.DrawGraphs(s1,s2,p1,p2,O,mA,B,C,D,m1,m2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
