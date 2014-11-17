# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def SVPCooGYtlqq():
    pspict,fig = SinglePicture("SVPCooGYtlqq")
    pspict.dilatation_X(3/90)
    pspict.dilatation_Y(5/80)

    pspict.Mx_acceptable_BB=300
    pspict.My_acceptable_BB=60

    pspict.axes.do_mx_enlarge=False
    pspict.axes.do_my_enlarge=False
    pspict.grid.do_mx_enlarge=False
    pspict.grid.do_my_enlarge=False

    seg=Segment(  Point(0,0),Point(90,30) )
    
    pspict.axes.single_axeX.Dx=30
    pspict.axes.single_axeY.Dx=10
    pspict.axes.single_axeX.put_mark(0.2,-45,u"durée (en \si{\minute})",automatic_place=(pspict,"corner"))
    pspict.axes.single_axeY.put_mark(0.2,0,"distance parcourue (en \si{\kilo\meter})",automatic_place=(pspict,"corner"))
    pspict.grid.Dx=15
    pspict.grid.Dy=10
    pspict.DrawGraphs(seg)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
