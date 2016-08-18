# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
from phystricksCommons import Pyramide

dilatation=1

def LYJooVYRkMy():
    pspict,fig = SinglePicture("LYJooVYRkMy")
    pspict.dilatation_X(dilatation)
    pspict.dilatation_Y(dilatation)

    x=var('x')
    pyramide=Pyramide(4,1,0.5)
    pyramide.centres[(0,0)].put_mark(0.0,0,"\( 1\)",pspict=pspict,position="center")
    pyramide.centres[(1,0)].put_mark(0.0,0,"\( 1\)",pspict=pspict,position="center")
    pyramide.centres[(2,0)].put_mark(0.0,0,"\( -1\)",pspict=pspict,position="center")
    pyramide.centres[(3,0)].put_mark(0.0,0,"\( -1\)",pspict=pspict,position="center")

    pspict.DrawGraphs(pyramide)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def SCVooUjmESN():
    pspict,fig = SinglePicture("SCVooUjmESN")
    pspict.dilatation_X(dilatation)
    pspict.dilatation_Y(dilatation)

    x=var('x')
    pyramide=Pyramide(4,1,0.5)
    pyramide.centres[(0,0)].put_mark(0.0,0,"\( -2\)",pspict=pspict,position="center")
    pyramide.centres[(1,0)].put_mark(0.0,0,"\( +2\)",pspict=pspict,position="center")
    pyramide.centres[(2,0)].put_mark(0.0,0,"\( -2\)",pspict=pspict,position="center")
    pyramide.centres[(3,0)].put_mark(0.0,0,"\( -2\)",pspict=pspict,position="center")

    pspict.DrawGraphs(pyramide)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def SWHooJzpmlM():
    SCVooUjmESN()
    LYJooVYRkMy()
