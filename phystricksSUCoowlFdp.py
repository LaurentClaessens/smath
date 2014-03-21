# -*- coding: utf8 -*-
from phystricks import *
def SUCoowlFdp():

    pspict,fig = SinglePicture("SUCoowlFdp")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    fig.specific_needs="""\makeatletter\@ifundefined{vect}{\\newcommand{\\vect}[1]{\overrightarrow{#1}}}{}\makeatother"""

    O=Point(0,0)
    A=Point(3,1)
    B=Point(-1,1)
    C=Point(-3,2)
    F=B+(-1,0)

    O.put_mark(0.2,-45,"\( O\)",automatic_place=(pspict,"corner"))
    A.put_mark(0.2,45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,180+45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,90+45,"\( C\)",automatic_place=(pspict,"corner"))
    F.put_mark(0.2,180+45,"\( F\)",automatic_place=(pspict,"corner"))

    pspict.force_math_bounding_box( C+(-1,1) )
    pspict.force_math_bounding_box( A+(1,0) )

    vOA=AffineVector(O,A)
    vBC=AffineVector(B,C).fix_origin(A)
    E=vBC.F
    E.put_mark(0.2,45,"\( E\)",automatic_place=(pspict,"corner"))

    v=AffineVector(O,E)

    vOA.parameters.color="red"
    vBC.parameters.color="red"
    v.parameters.color="blue"
    v.put_mark(0.2,45,r"\(  \vect{ v } \)",mark_point=v.center(),automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(O,A,C,B,F,E,vOA,vBC,v)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
