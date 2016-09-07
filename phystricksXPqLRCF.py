# -*- coding: utf8 -*-
from phystricks import *

x=var('x')
f=phyFunction(-x+1).graph(-2,4)
g=phyFunction(2*x-3).graph(-1,3.5)
h=phyFunction(-3*x+1).graph(-1,2)


g.parameters.color="brown"
h.parameters.color="red"            # Cette couleur est prononcée explicitement dans le texte.

def XPqLRCF():
    pspict,fig = SinglePicture("XPqLRCF")
    pspict.dilatation(0.8)

    f.put_mark(0.2,0,"\( f\)",pspict=pspict,position="W")
    g.put_mark(0.2,0,"\( g\)",pspict=pspict,position="W")
    h.put_mark(0.2,0,"\( h\)",pspict=pspict,position="W")

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


def VXFxyni():
    pspict,fig = SinglePicture("VXFxyni")
    pspict.dilatation(1)

    f.put_mark(0.2,0,"\( f\)",pspict=pspict,position="W")
    g.put_mark(0.2,0,"\( g\)",pspict=pspict,position="W")
    h.put_mark(0.2,0,"\( h\)",pspict=pspict,position="W")

    K=g.get_point(2)
    K.put_mark(0.2,K.advised_mark_angle(pspict),"\( K\)",pspict=pspict)
    #K.put_mark(0.2,90,"\( K\)",pspict=pspict)

    pspict.DrawGraphs(f,g,h,K)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
