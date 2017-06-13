# -*- coding: utf8 -*-
from phystricks import *
def PORLooZXtmpv():
    from communPhys import parallelog
    pspict,fig = SinglePicture("PORLooZXtmpv")
    pspict.dilatation(0.5)

    A=Point(0,0)
    B=Point(-1,-1)
    C=Point(1,-1)

    parallelog(A,B,C,points_names="ABCD",fig=fig,pspict=pspict)
