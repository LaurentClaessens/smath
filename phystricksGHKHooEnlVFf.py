# -*- coding: utf8 -*-
from phystricks import *
def GHKHooEnlVFf():
    pspict,fig = SinglePicture("GHKHooEnlVFf")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(1)

    M=Point(0,0)
    N=Point(0,4)
    L=Point(1,0.5)
    K=Point(-2,3.5)

    d1=Segment(L,K)
    d2=Segment(M,N)
    O=Intersection(d1,d2)[0]

    pr1=0.3
    pr2=0.8
    A=Segment(O,K).get_point_proportion(pr1)
    D=Segment(O,N).get_point_proportion(pr1)


    B=Segment(O,K).get_point_proportion(pr2)
    C=Segment(O,N).get_point_proportion(pr2)

    s1=Segment(B,C).dilatation(1.5)
    s2=Segment(A,D).dilatation(1.5)

    m1=Segment(B,A).get_code(n=2,d=0.1,l=0.2,angle=80,pspict=pspict)
    m2=Segment(A,O).get_code(n=2,d=0.1,l=0.2,angle=80,pspict=pspict)

    O.put_mark(0.2,angle=45,text="\( O\)",pspict=pspict)
    C.put_mark(0.2,angle=45,added_angle=0,text="\( C\)",pspict=pspict)
    D.put_mark(0.2,angle=45,added_angle=0,text="\( D\)",pspict=pspict)
    M.put_mark(0.2,angle=None,text="\( M\)",pspict=pspict)
    N.put_mark(0.2,angle=None,text="\( N\)",pspict=pspict)
    K.put_mark(0.2,angle=None,text="\( K\)",pspict=pspict)
    L.put_mark(0.2,angle=None,text="\( L\)",pspict=pspict)

    #mA=Angle(s2.I,A,L,r=0.1).get_mark(0.2,angle=None,text="\( A\)",pspict=pspict)
    mA=Angle(D,A,B,r=0.1).get_mark(0.2,angle=None,text="\( A\)",pspict=pspict)
    mB=Angle(s1.F,B,K,r=0.1).get_mark(0.2,angle=None,text="\( B\)",pspict=pspict)

    pspict.comment="The marks $A$ and $B$ are in the center of the angle and at reasonable distance."
    no_symbol(O,A,B,C,D)
    pspict.DrawGraphs(d1,d2,O,A,B,C,D,s1,s2,m1,m2,mA,mB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
