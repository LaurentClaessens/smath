# -*- coding: utf8 -*-
from phystricks import *
def IllusionNHwEtp():
    pspict,fig = SinglePicture("IllusionNHwEtp")
    pspict.dilatation(1)

    perspective=ObliqueProjection(45,sqrt(2)/2)

    l=3
    P=(0,0)
    cubesP=[]
    for i in range(0,4):
        cubesP.append(perspective.cuboid( P,l,l,l ))
        Q=cubesP[-1].c2[3]
        P=(Q.x,Q.y)
    cubesP.reverse()    # Ainsi les plus éloignés sont tracés en premier.
    for cub in cubesP:
        cub.make_opaque()
        pspict.DrawGraphs(cub)

    fig.conclude()
    fig.write_the_file()
