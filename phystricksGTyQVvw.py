# -*- coding: utf8 -*-
from phystricks import *
def GTyQVvw():
    pspict,fig = SinglePicture("GTyQVvw")
    fig.specific_needs="""\makeatletter\@ifundefined{vect}{\\newcommand{\\vect}[1]{\overrightarrow{#1}}}{}\makeatother"""
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    A=Point(0,2)
    B=Point(1,3)
    C=Point(4,2)
    D=Point(3,0)

    M=Point(3,3)
    N=Point(3,2)
    K=Point(1,1)
    L=Point(1,0)

    M.put_mark(0.2,45,"\( M\)",pspict=pspict,position="corner")
    N.put_mark(0.2,45,"\( N\)",pspict=pspict,position="corner")
    K.put_mark(0.2,45,"\( K\)",pspict=pspict,position="corner")
    L.put_mark(0.2,45,"\( L\)",pspict=pspict,position="corner")

    u=AffineVector(A,B)
    v=AffineVector(C,D)
    u.put_mark(0.2,None,"\( \\vect{ u }\)",pspict=pspict,position="corner")
    v.put_mark(0.2,None,"\( \\vect{ v }\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(u,v,M,N,K,L)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
