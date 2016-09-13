# -*- coding: utf8 -*-
from phystricks import *
def figureLEOvqez():
    pspict,fig = SinglePicture("figureLEOvqez")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,2)
    C=Point(B.x,A.y)

    A.put_mark(0.2,180,"\( A\)",pspict=pspict)
    B.put_mark(0.2,45,"\( B\)",pspict=pspict)

    A.parameters.symbol="*"
    B.parameters.symbol="x"

    AB=AffineVector(A,B)
    AC=AffineVector(A,C)
    CB=AffineVector(C,B)

    AC.put_mark(0.2,-90,"\( x_B-x_A\)",pspict=pspict,mark_point=AC.midpoint())
    # TODO : un truc bizare est que la croix de B n'apparaît pas à cause de la ligne suivante :
    CB.put_mark(0.2,0,"\( y_B-y_A\)",pspict=pspict,mark_point=CB.midpoint())

    AB.parameters.color="blue"
    AC.parameters.color="red"
    CB.parameters.color="red"

    pspict.DrawGraphs(AB,AC,CB,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
