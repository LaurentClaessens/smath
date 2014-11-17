# -*- coding: utf8 -*-

import string

from phystricks import *
def GARYooJCnpFS():
    pspicts,figs = IndependentPictures("GARYooJCnpFS",2)
    for psp in pspicts: 
        psp.dilatation(1)

    A=Point(0,0)
    B=Point(4,1)
    C=Point(3,3)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspicts)
    for psp in pspicts :
        psp.DrawGraphs(triangle)
    
    for i in [0,1,2]:
        cot=triangle.edges[ (i+1)%3 ].copy()
        P=triangle.vertices[i]
        M=cot.midpoint()
        med=Segment(M,P).dilatation(1.5)
        med.parameters.style="dashed"

        pspicts[0].DrawGraphs(med)

        cot.divide_in_two(n=i+1,d=0.1,l=0.3,pspict=pspicts)
        pspicts[1].DrawGraphs(cot,med)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
