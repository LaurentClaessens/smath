# -*- coding: utf8 -*-
from phystricks import *

from phystricksUCAOooLGwJUe import thales

def VXDJooBGRpbL():
    pspict,fig = SinglePicture("VXDJooBGRpbL")
    pspict.dilatation(3)

    I=Point(0,0)
    K=Point(-1.5,2)
    J=Point(0.5,2)
    L,M=thales(  I,K,J, 0.45,'I',"K","J","L","M",pspict,rotate=180 )

    m1=Segment(K,J).get_mark(0.1,None,"\( 7\)",automatic_place=(pspict,"corner"))
    m2=Segment(J,L).get_mark(0.1,None,"\( 8\)",automatic_place=(pspict,"corner"))
    m3=Segment(L,I).get_mark(0.1,None,"\( 2\)",automatic_place=(pspict,"corner"))
    m4=Segment(M,I).get_mark(-0.1,None,"\( 5\)",automatic_place=(pspict,"corner"))

    no_symbol(K,J,M,L,I)

    pspict.DrawGraphs(m1,m2,m3,m4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

