# -*- coding: utf8 -*-
from phystricks import *

def parallelog(A,B,C,points_names="ABCD",fig=None,pspict=None):
    D=A+C-B
    parall=Polygon(A,B,C,D)
    parall.put_mark(0.2,points_names=points_names,pspict=pspict)
    #parall.put_mark(0.2,text_list=["\( A\)","\( B\)","\( C\)","\( D\)"],pspict=pspict)


    s1=Segment(A,B)
    s2=Segment(B,C)

    no_symbol(parall.vertices)

    pspict.DrawGraphs(s1,s2,parall.vertices[:-1])

    pspict.math_BB.append(D)
    pspict.math_BB.xmax+=1
    pspict.math_BB.ymax+=1
    pspict.math_BB.xmin-=1
    pspict.math_BB.ymin-=1

    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def CFRQooRohKqN():
    pspict,fig = SinglePicture("CFRQooRohKqN")
    pspict.dilatation(0.5)

    A=Point(0,0)
    B=Point(3,1)
    C=Point(4,3)

    parallelog(A,B,C,points_names="KLMN",fig=fig,pspict=pspict)
    pspict.comment="The grid is exactly one more than the points"

def PORLooZXtmpv():
    pspict,fig = SinglePicture("PORLooZXtmpv")
    pspict.dilatation(0.5)

    A=Point(0,0)
    B=Point(-1,-1)
    C=Point(1,-1)

    parallelog(A,B,C,points_names="ABCD",fig=fig,pspict=pspict)

def XQKVooWaptGc():
    pspict,fig = SinglePicture("XQKVooWaptGc")
    pspict.dilatation(0.5)
    A=Point(-1,-1)
    B=Point(0,0)
    C=Point(1,-1)
    parallelog(A,B,C,points_names="STUV",fig=fig,pspict=pspict)

def ZGZNooJZBEwl():
    pspict,fig = SinglePicture("ZGZNooJZBEwl")
    pspict.dilatation(0.5)
    A=Point(0,0)
    B=Point(1,1)
    C=Point(3.5,1)
    parallelog(A,B,C,points_names="RDEF",fig=fig,pspict=pspict)


def FTKEooCLvbNp():
    CFRQooRohKqN()
    PORLooZXtmpv()
    XQKVooWaptGc()
    ZGZNooJZBEwl()
