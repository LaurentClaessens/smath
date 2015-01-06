# -*- coding: utf8 -*-

from phystricks import *

def thales(A,B,C,prop,ma,mb,mc,mi,mj,pspict,rotate=0):
    trig=Polygon(A,B,C)
    trig.put_mark(0.2,text_list=["\( {}\)".format(ma),"\( {}\)".format(mb),"\( {}\)".format(mc)],pspict=pspict)
    I=Segment(A,C).get_point_proportion(prop)
    J=Segment(A,B).get_point_proportion(prop)
    I.put_mark(0.2,I.advised_mark_angle+rotate,"\( {}\)".format(mi),automatic_place=(pspict,"corner"))
    J.put_mark(0.2,J.advised_mark_angle+180+rotate,"\( {}\)".format(mj),automatic_place=(pspict,"corner"))
    seg=Segment(I,J)
    pspict.DrawGraphs(trig,seg,I,J)
    return I,J

def CSUHooJIJzsW():
    pspict,fig = SinglePicture("CSUHooJIJzsW")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    N=Point(2,2)
    M=Point(1,3)
    B,C=thales(  A,N,M, 0.53,'A',"N","M","B","C",pspict )

    m1=Segment(C,A).get_mark(0.2,None,"\( 3\)",automatic_place=(pspict,"corner"))
    m2=Segment(B,C).get_mark(0.2,None,"\( 2\)",automatic_place=(pspict,"corner"))
    m3=Segment(A,M).get_measure(-0.6,0.1,None,"\( 4.5\)",automatic_place=(pspict,"E"))
    m4=Segment(M,N).get_mark(0.2,None,"\( 6\)",automatic_place=(pspict,"E"))

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def WRBDooZhkhcW():
    pspict,fig = SinglePicture("WRBDooZhkhcW")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    B=Point(0,0)
    A=Point(1,-1)
    C=Point(1.5,3)
    T,S=thales(  C,B,A, 0.73,'C',"B","A","T","S",pspict )

    m1=Segment(S,C).get_mark(0.1,None,"\( 5\)",automatic_place=(pspict,"corner"))
    m2=Segment(T,S).get_mark(0.1,None,"\( 3\)",automatic_place=(pspict,"corner"))
    m3=Segment(B,C).get_measure(-0.6,0.1,None,"\( 13\)",automatic_place=(pspict,"corner"))
    m4=Segment(C,A).get_measure(-0.5,0.1,None,"\( 6.5\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def QMJQooQratnO():
    pspict,fig = SinglePicture("QMJQooQratnO")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(-0.5,-3)
    C=Point(1.5,-3.5)
    M,P=thales(  A,B,C, 0.52,'A',"B","C","M","P",pspict )

    m1=Segment(A,M).get_mark(0.1,None,"\( 5\)",automatic_place=(pspict,"corner"))
    m2=Segment(P,M).get_mark(-0.1,None,"\( 3\)",automatic_place=(pspict,"corner"))
    m3=Segment(P,B).get_mark(-0.1,None,"\( 2\)",automatic_place=(pspict,"corner"))
    m4=Segment(B,A).get_measure(-0.6,0.1,None,"\( 6\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def BJOSooIdFKWA():
    pspict,fig = SinglePicture("BJOSooIdFKWA")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    I=Point(0,0)
    K=Point(-1.5,2)
    J=Point(0.5,2)
    L,M=thales(  I,K,J, 0.65,'I',"K","J","L","M",pspict,rotate=180 )

    m1=Segment(K,J).get_mark(0.1,None,"\( 7\)",automatic_place=(pspict,"corner"))
    m2=Segment(J,L).get_mark(0.1,None,"\( 2\)",automatic_place=(pspict,"corner"))
    m3=Segment(L,I).get_mark(0.1,None,"\( 8\)",automatic_place=(pspict,"corner"))
    m4=Segment(M,I).get_mark(-0.1,None,"\( 5\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


def UCAOooLGwJUe():
    BJOSooIdFKWA()
    QMJQooQratnO()
    WRBDooZhkhcW()
    CSUHooJIJzsW()
