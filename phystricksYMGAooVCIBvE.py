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

    R1=c1.get_point(200)
    R2=c2.get_point(100)

    l1=Segment(L,R1).get_measure(0,0.1,None,"\( 5\)",automatic_place=(pspict,"corner"))
    l2=Segment(M,R2).get_measure(0,0.1,None,"\( 7\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs( seg,L,M,c1,c2,l1,l2 )
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
