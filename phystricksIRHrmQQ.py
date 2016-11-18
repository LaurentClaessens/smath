# -*- coding: utf8 -*-
from phystricks import *

def pyth(A,B,nom,color,pspict):
    K=Point(A.x,B.y)
    K.put_mark(0.2,text="\( {}\)".format(nom),pspict=pspict,position="S")

    AK=Segment(A,K)
    BK=Segment(B,K)
    AK.parameters.color=color
    AK.parameters.style="dashed"
    BK.parameters.color=AK.parameters.color
    BK.parameters.style=AK.parameters.style

    pspict.DrawGraphs(AK,BK,K)
    

def IRHrmQQ():
    pspict,fig = SinglePicture("IRHrmQQ")
    pspict.dilatation(0.7)

    A=Point(-1,2)
    B=Point(2,0)
    C=Point(8,9)

    A.put_mark(0.2,text="\( A\)",pspict=pspict,position="S")
    B.put_mark(0.2,text="\( B\)",pspict=pspict,position="S")
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="S")


    triangle=Polygon(A,B,C)

    pyth(B,A,"K","cyan",pspict)
    pyth(C,B,"L","red",pspict)
    pyth(A,C,"M","blue",pspict)

    pspict.DrawGraphs(A,B,C,triangle)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
