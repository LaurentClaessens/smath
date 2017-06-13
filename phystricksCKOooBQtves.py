# -*- coding: utf8 -*-
from phystricks import *


def makeCKO(pspict,num):
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    l=10
    a1=40
    a2=75

    A=Point(0,0)
    B=Point(l,0)

    seg1=Segment(A,B).dilatation(1.3)
    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")
    
    m=Segment(A,B).midpoint()
    m.parameters.symbol=""
    m.put_mark(0.2,text="\( {}\)".format(l),pspict=pspict,position="N")


    K=Circle(A,12).get_point(a1)
    L=Circle(B,9).get_point(180-a2)

    seg2=Segment(A,K)
    seg3=Segment(B,L)

    seg2.parameters.style='dashed'
    seg3.parameters.style='dashed'

    C=Intersection(seg2,seg3)[0]
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="S")

    angle1=AngleAOB(B,A,K)
    angle2=AngleAOB(L,B,A)
    angle1.put_mark(text="\( {}\)".format(a1),pspict=pspict)
    angle2.put_mark(text="\( {}\)".format(a2),pspict=pspict)

    edge1=Segment(A,B)
    edge2=Segment(A,C)
    edge3=Segment(B,C)

    if num==0:
        pspict.DrawGraphs(A,B,seg1,m)
    if num==1 :
        pspict.DrawGraphs(A,B,seg1,seg2,seg3,angle1,angle2,m)
    if num==2:
        pspict.DrawGraphs(A,B,C,angle1,angle2,edge1,edge2,edge3,m)


def EIQooXptWUa():
    pspict,fig = SinglePicture("EIQooXptWUa")
    makeCKO(pspict,0)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def GUEooKQcWgv():
    pspict,fig = SinglePicture("GUEooKQcWgv")
    makeCKO(pspict,1)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def MQJooVtXTde():
    pspict,fig = SinglePicture("MQJooVtXTde")
    makeCKO(pspict,2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
