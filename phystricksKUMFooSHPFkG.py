# -*- coding: utf8 -*-
from phystricks import *
def KUMFooSHPFkG():
    pspict,fig = SinglePicture("KUMFooSHPFkG")
    pspict.dilatation(1)


    A=Point(0,0)
    B=Circle(A,3).get_point(20)
    D=Segment(A,B).rotation(90).F
    C=Segment(D,A).rotation(90).F

    carre=Polygon(A,B,C,D)
    carre.put_mark(0.2,pspict=pspict)

    pspict.DrawGraphs(carre)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
