# -*- coding: utf8 -*-
from phystricks import *

def figureEHyIMRQ():
    pspict,fig = SinglePicture("figureEHyIMRQ")
    pspict.dilatation_X(0.003)
    pspict.dilatation_Y(0.5)

    pspict.Mx_acceptable_BB=5000
    pspict.mx_acceptable_BB=-400

    moustache1=Moustache(500,1000,1400,1500,2300,h=0.5,delta_y=1)
    moustache2=Moustache(300,950,1500,3200,4000,h=0.5,delta_y=2)
    moustache3=Moustache(700,800,950,1800,3000,h=0.5,delta_y=3)
    moustache4=Moustache(1000,1600,1900,2300,2500,h=0.5,delta_y=4)
    moustache5=Moustache(1300,1700,1900,2050,2200,h=0.5,delta_y=5)

    moustache1.put_mark(0.3,0,"\( A\)",pspict=pspict)
    moustache2.put_mark(0.3,0,"\( B\)",pspict=pspict)
    moustache3.put_mark(0.3,0,"\( C\)",pspict=pspict)
    moustache4.put_mark(0.3,0,"\( D\)",pspict=pspict)
    moustache5.put_mark(0.3,0,"\( E\)",pspict=pspict)

    pspict.DrawGraphs(moustache1,moustache2,moustache3,moustache4,moustache5)
    pspict.axes.single_axeX.Dx=500
    pspict.axes.single_axeY.no_graduation()
    pspict.grid.Dx=200
    pspict.grid.draw_horizontal_grid=False
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

# TODO : il faudrait ne tracer que l'axe horizontal.
