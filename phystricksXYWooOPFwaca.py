# -*- coding: utf8 -*-
from phystricks import *
def XYWooOPFwaca():
    from communPhys import contour
    pspict,fig = SinglePicture("XYWooOPFwaca")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    contour(3,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
