# -*- coding: utf8 -*-
from phystricks import *
def NWVMooKshXYo():
    pspict,fig = SinglePicture("NWVMooKshXYo")
    pspict.dilatation(1)

    A=Point(0,0)
    N=Point(4,0)
    D=Point(1,3)

    triangle=Polygon(A,N,D)
    triangle.put_mark(0.2,text_list=["\( A\)","\( N\)","\( D\)"],pspict=pspict)

    J=triangle.edges[2].midpoint()
    K=triangle.edges[1].midpoint()
    J.put_mark(0.2,J.advised_mark_angle+180,"\( J\)",automatic_place=(pspict,"corner"))
    K.put_mark(0.2,K.advised_mark_angle+180,"\( K\)",automatic_place=(pspict,"corner"))
    seg=Segment(J,K)
    
    triangle.edges[1].divide_in_two(n=1,d=0.1,l=0.3,angle=45,pspict=pspict)
    triangle.edges[2].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)

    mes=triangle.edges[0].get_measure(0.2,0.1,-90,"\SI{7.8}{\centi\meter}",automatic_place=(pspict,"N"))

    pspict.DrawGraphs(triangle,seg,mes,J,K)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
