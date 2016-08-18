# -*- coding: utf8 -*-
from phystricks import *
def GLKFooKwvxSl():
    pspict,fig = SinglePicture("GLKFooKwvxSl")
    pspict.dilatation(0.7)

    A=Point(-2,1)
    A.put_mark(0.2,A.angle(),"\( A\)",pspict=pspict,position="corner")


    B=Point(4,1)
    C=Point(2,-3)
    B.put_mark(0.2,B.angle(),"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,C.angle(),"\( C\)",pspict=pspict,position="corner")

    
    pspict.math_BB.append(A,pspict=pspict)
    pspict.math_BB.append(B,pspict=pspict)
    pspict.math_BB.append(C,pspict=pspict)
    pspict.math_BB.append(Point(-1,-1),pspict=pspict)
    pspict.math_BB.append(Point(1,-1),pspict=pspict)
    pspict.math_BB.append(Point(1,3),pspict=pspict)

    pspict.DrawGraphs(A)
    #pspict.DrawGraphs(B,C)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
