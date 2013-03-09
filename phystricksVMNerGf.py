# -*- coding: utf8 -*-
from phystricks import *

def VMNerGf():
    pspict,fig = SinglePicture("VMNerGf")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(4,0)
    v1=Vector(1,1).fix_origin(A)
    v2=Vector(-1,3).fix_origin(B)

    A.put_mark(0.2,-90,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,-90,"\( B\)",automatic_place=pspict)

    pspict.DrawGraphs(A,B,v1,v2,A,B)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
