# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def HYKooCotyT():
    pspict,fig = SinglePicture("HYKooCotyT")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)


    fig.specific_needs="""\makeatletter\@ifundefined{vect}{\\newcommand{\\vect}[1]{\overrightarrow{#1}}}{}\makeatother"""

    A=Point(1,1)
    B=A+(1,2)
    
    C=Point(-2,0)
    D=C+(4,-2)

    L=D+(1,0)
    L.put_mark(0.2,-45,"\( L\)",automatic_place=(pspict,"corner"))

    u1=AffineVector(A,B)
    u2=AffineVector(C,D)


    u3=(3/2)*u2
    pspict.force_math_bounding_box( u3 )

    u1.put_mark(0.2,45,"\( \\vect{ u_1 }\)",automatic_place=(pspict,"corner"))
    u2.put_mark(0.2,45,"\( \\vect{ u_2 }\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(u1,u2,L)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
