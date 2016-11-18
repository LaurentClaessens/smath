# -*- coding: utf8 -*-
from phystricks import *
def LXWooEsxsx():
    pspict,fig = SinglePicture("LXWooEsxsx")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    fig.specific_needs="""\makeatletter\@ifundefined{vect}{\\newcommand{\\vect}[1]{\overrightarrow{#1}}}{}\makeatother"""

    x=var('x')
    A1=Point(0,0)
    B1=Point(1,2)
    B2=Point(-0.5,1.5)

    m1=Vector(3,-1)
    m2=Vector(2,0)

    u1=m1.fix_origin(A1)
    v1=0.5*m1.fix_origin(B1)

    u2=m2.fix_origin(A1)
    v2=0.5*m2.fix_origin(B2)

    u3=AffineVector(  Point(5,3),Point(2,2) )
    v3=AffineVector( Point(1,1),Point(0,-2) )

    u1.put_mark(0.2,45,"\( \\vect{ u_1 }\)",pspict=pspict,position="corner")
    v1.put_mark(0.2,-45,"\( \\vect{ v_1 }\)",pspict=pspict,position="corner")
    u2.put_mark(0.2,45,"\( \\vect{ u_2 }\)",pspict=pspict,position="corner")
    v2.put_mark(0.2,text="\( \\vect{ v_2 }\)",pspict=pspict,position="S")
    u3.put_mark(0.2,45,"\( \\vect{ u_3 }\)",pspict=pspict,position="corner")
    v3.put_mark(0.2,-45,"\( \\vect{ v_3 }\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(u1,v1,u2,v2,u3,v3)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
