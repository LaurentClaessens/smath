# -*- coding: utf8 -*-
from phystricks import *
def BPZooBCyuyK():
    from communPhys import contour
    pspict,fig = SinglePicture("BPZooBCyuyK")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    contour(4,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
