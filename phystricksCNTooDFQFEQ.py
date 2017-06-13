# -*- coding: utf8 -*-

from phystricks import *

from phystricksCommons import Pyramide

dilatation=1

def CPVooSIVPHp():
    pspict,fig = SinglePicture("CPVooSIVPHp")
    pspict.dilatation_X(dilatation)
    pspict.dilatation_Y(dilatation)

    x=var('x')
    pyramide=Pyramide(4,1,0.5)
    pyramide.centres[(1,0)].put_mark(0.0,0,"\( -1\)",pspict=pspict,position="center")
    pyramide.centres[(3,0)].put_mark(0.0,0,"\( +2\)",pspict=pspict,position="center")
    pyramide.centres[(0,2)].put_mark(0.0,0,"\( -4\)",pspict=pspict,position="center")
    pyramide.centres[(2,0)].put_mark(0.0,0,"\( -3\)",pspict=pspict,position="center")

    pspict.DrawGraphs(pyramide)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def HQQooVpesUc():
    pspict,fig = SinglePicture("HQQooVpesUc")
    pspict.dilatation_X(dilatation)
    pspict.dilatation_Y(dilatation)

    x=var('x')
    pyramide=Pyramide(4,1,0.5)
    pyramide.centres[(3,0)].put_mark(0.0,0,"\( +5\)",pspict=pspict,position="center")
    pyramide.centres[(1,1)].put_mark(0.0,0,"\( -6\)",pspict=pspict,position="center")
    pyramide.centres[(0,2)].put_mark(0.0,0,"\( -24\)",pspict=pspict,position="center")
    pyramide.centres[(0,3)].put_mark(0.0,0,"\( -2160\)",pspict=pspict,position="center")

    pspict.DrawGraphs(pyramide)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
