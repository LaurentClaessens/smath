# -*- coding: utf8 -*-
from phystricks import *

def axial_symetry(P,axe):
    Q=P.projection(axe)
    v=AffineVector(P,Q)
    return Q+v


def KREWooIrMfCQ():
    pspict,fig = SinglePicture("KREWooIrMfCQ")
    pspict.dilatation(1)

    axe=Segment(  Point(0,-5),Point(3,5)  )

    A=Point(4,0)
    Ap=axial_symetry(A,axe)

    A.put_mark(0.2,0,"\( A\)",automatic_place=(pspict,"corner"))
    Ap.put_mark(0.2,0,"\( A'\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(axe,A,Ap)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
