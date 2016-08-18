# -*- coding: utf8 -*-
from phystricks import *
def AWKEooFytNYo():
    pspict,fig = SinglePicture("AWKEooFytNYo")
    pspict.dilatation(0.7)

    A=Point(0,0)
    B=Point(4,-0.5)
    C=Point(6,-2)

    A.put_mark(0.2,90+45,"\( Alala\)",pspict=pspict,position="corner")
    B.put_mark(0.2,45,"\( Bobobo\)",pspict=pspict,position="corner")
    C.put_mark(0.2,-45,"\( Catata\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(A,B,C)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

