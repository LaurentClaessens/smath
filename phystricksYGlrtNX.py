# -*- coding: utf8 -*-
from phystricks import *
f=LagrangePolynomial( [Point(-4,-2),Point(-3,0),Point(-1.5,2),Point(0,0),Point(1,1),Point(2,3),Point(4,0)] ).graph(-4,4)

def QJLooNAToEq():
    pspictC,figC = SinglePicture("QJLooNAToEq")
    pspictC.dilatation_X(0.9)

    # La figure de correction

    A=f.get_point(2)
    A.put_mark(0.2,A.advised_mark_angle(pspictC),"\( A\)",pspict=pspictC,position="corner")

    Z1=f.get_point(-3)
    Z2=f.get_point(0)
    Z3=f.get_point(4)

    for i,Z in enumerate([Z1,Z2,Z3]):
        Z.put_mark(0.2,Z.advised_mark_angle(pspictC),"\( Z_{"+str(i+1)+"}\)",pspict=pspictC,position="corner")

    horiz=Segment(  Point(f.mx,1),Point(f.Mx,1) )
    horiz.parameters.color="red"

    pspictC.DrawGraphs(f,A,Z1,Z2,Z3,horiz)
    pspictC.DrawDefaultGrid()
    pspictC.DrawDefaultAxes()
    figC.no_figure()
    figC.conclude()
    figC.write_the_file()

def MLSSooNVfyOR():
    pspict,fig = SinglePicture("MLSSooNVfyOR")
    pspict.dilatation_X(0.9)


    pspict.DrawGraphs(f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
