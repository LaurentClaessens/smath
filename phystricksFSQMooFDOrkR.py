# -*- coding: utf8 -*-
from phystricks import *
def FSQMooFDOrkR():
    pspict,fig = SinglePicture("FSQMooFDOrkR")
    pspict.dilatation_X(1.2)
    pspict.dilatation_Y(1)

    mx=-4
    Mx=8

    O=Point(0,0)
    #A=Point(-3,0)
    #B=Point(4,0)

    K=Point(0.5,0)

    O.put_mark(0.2,-90,"\( O\)",pspict=pspict)
    #B.put_mark(0.2,-90,"\( B\)",pspict=pspict)
    K.put_mark(0.2,90,"\( \\frac{ 1 }{2}\)",pspict=pspict)

    for i in range(mx,0):
        A=Point(i,0)
        A.parameters.symbol=""
        if i%2==0 :
            A.put_mark(0.2,-90,"\(  {}\)".format(i),pspict=pspict)
        else:
            A.put_mark(0.2,-90,"\( {}\)".format(i),pspict=pspict)
        pspict.DrawGraphs(A)
    for i in range(0,floor(Mx)+1):
        A=Point(i,0)
        A.parameters.symbol=""
        A.put_mark(0.2,-90,"\( {}\)".format(i),pspict=pspict)
        pspict.DrawGraphs(A)

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.no_numbering()

    pspict.comment="An axe is graduated from -4 to 8. The graduations are under the axes and $1/2$ over the axe"
    pspict.DrawGraphs(axe,K)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
