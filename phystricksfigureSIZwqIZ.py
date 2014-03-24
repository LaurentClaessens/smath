# -*- coding: utf8 -*-
from phystricks import *
def figureSIZwqIZ():
    pspict,fig = SinglePicture("figureSIZwqIZ")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.5)

    x=var('x')

    F=[]
    F.append(phyFunction(x**2).graph(-2.5,2.5))
    F.append(phyFunction( 1-x**2 ).graph(-2,2))
    F.append(phyFunction( x+1 ).graph(-4,3))
    F.append(phyFunction( (x+2)**2 ).graph(-4,0.5))

    F[0].put_mark(0.2,0,"\( C_1\)",automatic_place=(pspict,"corner"))
    F[1].put_mark(0.2,0,"\( C_2\)",automatic_place=(pspict,"corner"))
    F[2].put_mark(0.2,0,"\( C_3\)",automatic_place=(pspict,"corner"))
    F[3].put_mark(0.2,0,"\( C_4\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(F)

    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
