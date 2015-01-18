# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def QXYWooOWHshl():
    pspicts,figs = IndependentPictures("QXYWooOWHshl",3)
    

    psp=pspicts[0]
    psp.dilatation_X(3/90)
    psp.dilatation_Y(5/80)

    psp.Mx_acceptable_BB=300
    psp.My_acceptable_BB=60

    psp.axes.do_mx_enlarge=False
    psp.axes.do_my_enlarge=False
    psp.grid.do_mx_enlarge=False
    psp.grid.do_my_enlarge=False

    seg=Segment(  Point(0,0),Point(90,30) )
    
    psp.axes.single_axeX.Dx=30
    psp.axes.single_axeY.Dx=10
    psp.axes.single_axeX.put_mark(0.2,-45,u"durée (en \si{\minute})",automatic_place=(pspicts,"corner"))
    psp.axes.single_axeY.put_mark(0.2,0,"distance parcourue (en \si{\kilo\meter})",automatic_place=(pspicts,"corner"))
    psp.grid.Dx=15
    psp.grid.Dy=10
    psp.DrawGraphs(seg)
    psp.DrawDefaultAxes()
    psp.DrawDefaultGrid()

    psp=pspicts[1]          # C'est celui-ci qui va être le bon
    psp.dilatation_X(3/90)
    psp.dilatation_Y(5/80)

    psp.Mx_acceptable_BB=300
    psp.My_acceptable_BB=60

    psp.axes.do_mx_enlarge=False
    psp.axes.do_my_enlarge=False
    psp.grid.do_mx_enlarge=False
    psp.grid.do_my_enlarge=False

    seg=Segment(  Point(0,0),Point(90,30) )
    
    psp.axes.single_axeX.Dx=30
    psp.axes.single_axeY.Dx=10
    psp.axes.single_axeX.put_mark(0.2,-45,u"durée (en \si{\minute})",automatic_place=(pspicts,"corner"))
    psp.axes.single_axeY.put_mark(0.2,0,"distance parcourue (en \si{\kilo\meter})",automatic_place=(pspicts,"corner"))
    psp.grid.Dx=15
    psp.grid.Dy=10
    psp.DrawGraphs(seg)
    psp.DrawDefaultAxes()
    psp.DrawDefaultGrid()

    psp=pspicts[2]
    psp.dilatation_X(3/90)
    psp.dilatation_Y(5/80)

    psp.Mx_acceptable_BB=300
    psp.My_acceptable_BB=60

    psp.axes.do_mx_enlarge=False
    psp.axes.do_my_enlarge=False
    psp.grid.do_mx_enlarge=False
    psp.grid.do_my_enlarge=False

    seg=Segment(  Point(0,0),Point(90,30) )
    
    psp.axes.single_axeX.Dx=30
    psp.axes.single_axeY.Dx=10
    psp.axes.single_axeX.put_mark(0.2,-45,u"durée (en \si{\minute})",automatic_place=(pspicts,"corner"))
    psp.axes.single_axeY.put_mark(0.2,0,"distance parcourue (en \si{\kilo\meter})",automatic_place=(pspicts,"corner"))
    psp.grid.Dx=15
    psp.grid.Dy=10
    psp.DrawGraphs(seg)
    psp.DrawDefaultAxes()
    psp.DrawDefaultGrid()


    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
