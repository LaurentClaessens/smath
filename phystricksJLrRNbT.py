# -*- coding: utf8 -*-
from phystricks import *
def JLrRNbT():
    pspict,fig = SinglePicture("JLrRNbT")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,-1)
    K=Point(3,1)
    L=Point(-2,0)
    M=L+(0,-1)
    S=K+L-M
    T=A+S-K

    A.put_mark(0.2,-45,"\( A\)",pspict=pspict,position="corner")
    K.put_mark(0.2,-45,"\( K\)",pspict=pspict,position="corner")
    L.put_mark(0.2,90+45,"\( L\)",pspict=pspict,position="corner")
    M.put_mark(0.2,180+45,"\( M\)",pspict=pspict,position="corner")
    T.put_mark(0.2,90+45,"\( T\)",pspict=pspict,position="corner")

    pspict.force_math_bounding_box( M+(-1,-1) )
    pspict.force_math_bounding_box( K+(1,1) )

    pspict.DrawGraphs(A,K,L,M,T)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
