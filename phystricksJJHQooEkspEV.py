# -*- coding: utf8 -*-
from phystricks import *
def JJHQooEkspEV():
    pspicts,figs = IndependentPictures("JJHQooEkspEV",3)
    for psp in pspicts :
        psp.dilatation_X(1)
        psp.dilatation_Y(0.7)

    S=Point(0,0)
    T=Point(3,-2)
    R=Point(3,4)

    triangle=Polygon(S,T,R)
    triangle.put_mark(0.2,text_list=['\( S\)',"\( T\)","\( R\)"],pspict=pspicts)

    M=triangle.edges[2].midpoint()
    M.put_mark(0.2,M.advised_mark_angle+180,"\( M\)",automatic_place=(pspicts,"corner"))
    O=triangle.edges[0].midpoint()
    O.put_mark(0.2,O.advised_mark_angle+180,"\( O\)",automatic_place=(pspicts,"corner"))

    seg=Segment(M,O)
    triangle.edges[2].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspicts)

    pspicts[0].DrawGraphs(triangle,seg,M,O)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
