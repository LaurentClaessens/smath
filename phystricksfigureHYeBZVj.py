# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def figureHYeBZVj():
    pspict,fig = SinglePicture("figureHYeBZVj")
    pspict.dilatation_Y(1/50)
    pspict.My_acceptable_BB=500

    x=var('x')
    Mx=15
    f11=phyFunction(150).graph(0,7)
    f12=phyFunction(25*x-25).graph(7,Mx)
    f2=phyFunction(30*x).graph(0,Mx)
    f3=phyFunction(50+25*x).graph(0,Mx)

    color1="blue"
    f11.parameters.color=color1
    f12.parameters.color=color1

    f2.parameters.color="red"
    f3.parameters.color="brown"

    g1=f2.graph(0,5)
    g2=f11.graph(5,7)
    g3=f12.graph(7,Mx)

    colorg="cyan"
    g1.parameters.color=colorg
    g2.parameters.color=colorg
    g3.parameters.color=colorg
    
    g1.wave(10,0.2)
    g2.wave(0.1,5)
    g3.wave(10,0.2)

    pspict.DrawGraphs(f11,f12,f2,f3,g1,g2,g3)
    pspict.axes.single_axeY.Dx=50
    pspict.grid.Dx=1
    pspict.grid.Dy=25
    pspict.grid.num_subX=0
    pspict.grid.num_subY=1
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
