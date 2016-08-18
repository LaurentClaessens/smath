# -*- coding: utf8 -*-
from phystricks import *
def MFWooBwnCkX():
    pspict,fig = SinglePicture("MFWooBwnCkX")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    l1=3
    l2=5
    l3=6

    A=Point(0,0)
    K=Point(1,2)
    S=Point(2,2)

    B=Circle(A,l1).get_point(80)
    L=Circle(K,l2).get_point(-30)
    T=Circle(S,l3).get_point(5)

    #A.put_mark(0.2,90,"\( A\)",pspict=pspict,position="corner")
    #B.put_mark(0.2,90,"\( B\)",pspict=pspict,position="corner")
    #K.put_mark(0.2,90,"\( K\)",pspict=pspict,position="corner")
    #L.put_mark(0.2,90,"\( L\)",pspict=pspict,position="corner")
    #S.put_mark(0.2,90,"\( S\)",pspict=pspict,position="corner")
    #T.put_mark(0.2,90,"\( T\)",pspict=pspict,position="corner")

    s1=Segment(A,B)
    s2=Segment(K,L)
    s3=Segment(S,T)

    pspict.DrawGraphs(s1,s2,s3,A,K,S,B,L,T)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
