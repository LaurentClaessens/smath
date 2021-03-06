# -*- coding: utf8 -*-
from phystricks import *
def JJHQooEkspEV():
    pspicts,figs = IndependentPictures("JJHQooEkspEV",3)
    for psp in pspicts :
        psp.dilatation_X(1)
        psp.dilatation_Y(0.5)

    S=Point(0,0)
    T=Point(3,-2)
    R=Point(3,4)

    triangle=Polygon(S,T,R)
    triangle.put_mark(0.5,text_list=['\( S\)',"\( T\)","\( R\)"],pspicts=pspicts)

    M=triangle.edges[2].midpoint()
    M.put_mark(0.5,M.advised_mark_angle(pspicts),added_angle=180,text="\( M\)",pspicts=pspicts,position="corner")
    O=triangle.edges[0].midpoint()
    O.put_mark(0.5,O.advised_mark_angle(pspicts),added_angle=180,text="\( O\)",pspicts=pspicts,position="corner")

    seg=Segment(M,O)
    SR2=triangle.edges[2].get_divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspicts=pspicts)
    ST2=triangle.edges[0].get_divide_in_two(n=1,d=0.1,l=0.3,angle=30,pspicts=pspicts)
    mesRT=triangle.edges[1].get_measure(0.2,0.1,text="\SI{4}{\centi\meter}",pspicts=pspicts,position="W")

    for psp in pspicts :
        psp.DrawGraphs(triangle,seg,M,O)
    
    pspicts[0].DrawGraphs(SR2)
    pspicts[1].DrawGraphs(triangle,seg,M,O)
    pspicts[2].DrawGraphs(SR2,ST2,mesRT)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
