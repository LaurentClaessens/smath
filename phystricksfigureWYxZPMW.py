# -*- coding: utf8 -*-
from phystricks import *

def suite1(n):
    return n+2
def suite2(n):
    return 2*n-5
def suite3(n):
    return -n+4
def suite4(n):
    return n**2-n+2

def figureWYxZPMW():
    pspicts,fig = MultiplePictures("figureWYxZPMW",4)
    pspicts[0].mother.caption=""
    pspicts[1].mother.caption=""
    pspicts[2].mother.caption=" "
    pspicts[3].mother.caption=" "

    for psp in pspicts:
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.5)
    pspicts[-1].dilatation_Y(0.3)
    pspicts[-1].axes.single_axeY.Dx=2
    

    U=[suite1,suite2,suite3,suite4]

    for i,psp in enumerate(pspicts):
        for k in range(0,5):
            psp.DrawGraphs(Point(k,U[i](k)))
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
