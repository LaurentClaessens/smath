# -*- coding: utf8 -*-

from phystricks import *

def thales(A,B,C,prop,ma,mb,mc,mi,mj,pspict):
    trig=Polygon(A,B,C)
    trig.put_mark(0.2,text_list=["\( {}\)".format(ma),"\( {}\)".format(mb),"\( {}\)".format(mc)],pspict=pspict)
    I=Segment(A,C).get_point_proportion(prop)
    J=Segment(A,B).get_point_proportion(prop)
    I.put_mark(0.2,I.advised_mark_angle,"\( {}\)".format(mi),automatic_place=(pspict,"corner"))
    J.put_mark(0.2,J.advised_mark_angle+180,"\( {}\)".format(mj),automatic_place=(pspict,"corner"))
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
    B,C=thales(  A,N,M, 0.5,'A',"N","M","B","C",pspict )

    m1=Segment(C,A).get_mark(0.2,None,"\( 3\)",automatic_place=(pspict,"corner"))
    m2=Segment(B,C).get_mark(0.2,None,"\( 2\)",automatic_place=(pspict,"corner"))
    m3=Segment(A,M).get_measure(-0.6,0.1,None,"\( 4.5\)",automatic_place=(pspict,"E"))
    m4=Segment(M,N).get_mark(0.2,None,"\( 6\)",automatic_place=(pspict,"E"))

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
