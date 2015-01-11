# -*- coding: utf8 -*-
from phystricks import *
def PQYKooJWKpVZ():
    pspict,fig = SinglePicture("PQYKooJWKpVZ")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(4,-2)
    C=Point(0,-2)
    D=Point(4,0)

    s1=Segment(A,B)
    s2=Segment(C,D).dilatation(1.3)

    I=Intersection(s1,s2)[0]

    alpha=Angle(A,I,C,0.4)
    beta=Angle(B,I,D,0.4)
    gamma=Angle(D,I,A,0.3)

    alpha.put_mark(0.2,alpha.advised_mark_angle,"\( a\)",automatic_place=(pspict,"center"))
    beta.put_mark(0.2,beta.advised_mark_angle,"\( b\)",automatic_place=(pspict,"center"))
    gamma.put_mark(0.2,gamma.advised_mark_angle,"\( c\)",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(s1,s2,alpha,beta,gamma)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
