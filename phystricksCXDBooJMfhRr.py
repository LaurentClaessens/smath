# -*- coding: utf8 -*-
from phystricks import *
def CXDBooJMfhRr():
    pspict,fig = SinglePicture("CXDBooJMfhRr")
    pspict.dilatation(0.63)


    a=1
    b=3

    A=Point(0,0)
    B=A+(2*a,0)
    C=B+(a,0)
    D=C+(0,-a)
    E=D+(-2*a,0)
    F=E+(0,-2*a)
    G=F+(-a,0)
    H=G+(0,a)
    I=H+(-a,0)
    J=I+(0,a)
    K=J+(a,0)

    poly=Polygon(A,B,C,D,E,F,G,H,I,J,K)
    poly.make_edges_independent()
    #poly.put_mark(0.2,pspict=pspict)

    for s in [  poly.edges[i] for i in [0,3,4]  ]:
        s.parameters.style="dashed"

    pspict.DrawGraphs(poly)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
