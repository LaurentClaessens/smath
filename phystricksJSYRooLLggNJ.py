# -*- coding: utf8 -*-
from phystricks import *

def unexo(a,b,c,noms,pspict):
    A=Point(a,0)
    B=Point(b,0)
    C=Point(c,0)
    O=Point(0,0)
    mx=min([a-1,b-1,c-1,-2])
    Mx=max([a+1,b+1,c+1,2])
    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.no_numbering()
    A.put_mark(0.2,angle=90,added_angle=0,text="\( {}\)".format(noms[0]),pspict=pspict)
    B.put_mark(0.2,angle=90,added_angle=0,text="\(  {}\)".format(noms[1]),pspict=pspict)
    C.put_mark(0.2,angle=90,added_angle=0,text="\( {}\)".format(noms[2]),pspict=pspict)
    O.put_mark(0.2,angle=-90,added_angle=0,text="\( 0\)",pspict=pspict)
    pspict.DrawGraphs(A,B,C,O,axe)

def JSYRooLLggNJ():
    pspicts,figs = IndependentPictures("JSYRooLLggNJ",4)

    unexo(2,3,5,"ABC",pspicts[0])
    unexo(-2,3,-5,"KLM",pspicts[1])
    unexo(0,3,-3,"STU",pspicts[2])
    unexo(-2,-3,1,"DEF",pspicts[3])

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
