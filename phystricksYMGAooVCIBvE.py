# -*- coding: utf8 -*-
from phystricks import *
def YMGAooVCIBvE():
    pspict,fig = SinglePicture("YMGAooVCIBvE")

    pspict.dilatation(0.5)

    L=Point(0,0)
    M=Point(15,0)
    seg=Segment(L,M)

    c1=Circle(L,5)
    c2=Circle(M,7)

    L.put_mark(0.2,180+45,"\( L\)",automatic_place=(pspict,"corner"))
    M.put_mark(0.2,-45,"\( M\)",automatic_place=(pspict,"corner"))

    c1.parameters.style="dashed"
    c2.parameters.style="dashed"

    pspict.DrawGraphs( seg,L,M,c1,c2 )
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
