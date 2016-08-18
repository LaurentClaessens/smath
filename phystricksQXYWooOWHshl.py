# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def QXYWooOWHshl():
    pspicts,figs = IndependentPictures("QXYWooOWHshl",4)
    

    pspicts[0].dilatation_X(2.5/90)
    pspicts[0].dilatation_Y(1/50)

    pspicts[0].Mx_acceptable_BB=300
    pspicts[0].My_acceptable_BB=300

    pspicts[0].axes.do_mx_enlarge=False
    pspicts[0].axes.do_my_enlarge=False
    #pspicts[0].axes.do_My_enlarge=False
    pspicts[0].grid.do_mx_enlarge=False
    pspicts[0].grid.do_my_enlarge=False

    f=LagrangePolynomial( [Point(0,0),Point(90,100),Point(45,25)]  ).graph(0,90)
    f.parameters.color="black"
    
    label_X=u"durée"
    label_Y=u"distance parcourue"
    pspicts[0].axes.single_axeX.Dx=30
    pspicts[0].axes.single_axeY.Dx=30
    pspicts[0].axes.single_axeX.put_mark(0.2,-45,label_X,pspict=pspicts,position="corner")
    pspicts[0].axes.single_axeY.put_mark(0.2,0,label_Y,pspict=pspicts,position="corner")
    pspicts[0].grid.Dx=15
    pspicts[0].grid.Dy=20
    pspicts[0].DrawGraphs(f)
    pspicts[0].DrawDefaultAxes()
    pspicts[0].DrawDefaultGrid()

                                  # C'est celui-ci qui va être le bon
    pspicts[1].dilatation_X(2.5/90)
    pspicts[1].dilatation_Y(1/50)

    pspicts[1].Mx_acceptable_BB=300
    pspicts[1].My_acceptable_BB=300

    pspicts[1].axes.do_mx_enlarge=False
    pspicts[1].axes.do_my_enlarge=False
    pspicts[1].grid.do_mx_enlarge=False
    pspicts[1].grid.do_my_enlarge=False

    seg=Segment(  Point(0,0),Point(90,100) )
    seg=Segment(  Point(0,0),Point(100,100*100/90) )
    
    pspicts[1].axes.single_axeX.Dx=30
    pspicts[1].axes.single_axeY.Dx=30
    pspicts[1].axes.single_axeX.put_mark(0.2,-45,label_X,pspict=pspicts,position="corner")
    pspicts[1].axes.single_axeY.put_mark(0.2,0,label_Y,pspict=pspicts,position="corner")
    pspicts[1].grid.Dx=15
    pspicts[1].grid.Dy=20
    pspicts[1].DrawGraphs(seg)
    pspicts[1].DrawDefaultAxes()
    pspicts[1].DrawDefaultGrid()



                                  # C'est celui-ci est pour la correction
    pspicts[3].dilatation_X(2.5/90)
    pspicts[3].dilatation_Y(1/50)

    pspicts[3].Mx_acceptable_BB=300
    pspicts[3].My_acceptable_BB=300

    pspicts[3].axes.do_mx_enlarge=False
    pspicts[3].axes.do_my_enlarge=False
    pspicts[3].grid.do_mx_enlarge=False
    pspicts[3].grid.do_my_enlarge=False

    seg=Segment(  Point(0,0),Point(90,100) )
    seg=Segment(  Point(0,0),Point(100,100*100/90) )
    
    P=Point(90,100)
    P.put_mark(0.2,90+45,"\( P\)",pspict=pspicts)
    P.parameters.symbol="*"

    pspicts[3].axes.single_axeX.Dx=30
    pspicts[3].axes.single_axeY.Dx=30
    pspicts[3].axes.single_axeX.put_mark(0.2,-45,label_X,pspict=pspicts,position="corner")
    pspicts[3].axes.single_axeY.put_mark(0.2,0,label_Y,pspict=pspicts,position="corner")
    pspicts[3].grid.Dx=15
    pspicts[3].grid.Dy=20
    pspicts[3].DrawGraphs(seg,P)
    pspicts[3].DrawDefaultAxes()
    pspicts[3].DrawDefaultGrid()



    pspicts[2].dilatation_X(2.5/90)
    pspicts[2].dilatation_Y(1/50)

    pspicts[2].Mx_acceptable_BB=300
    pspicts[2].My_acceptable_BB=300

    pspicts[2].axes.do_mx_enlarge=False
    pspicts[2].axes.do_my_enlarge=False
    pspicts[2].grid.do_mx_enlarge=False
    pspicts[2].grid.do_my_enlarge=False

    seg=Segment(  Point(0,100),Point(90,0) )
    
    pspicts[2].axes.single_axeX.Dx=30
    pspicts[2].axes.single_axeY.Dx=30
    pspicts[2].axes.single_axeX.put_mark(0.2,-45,label_X,pspict=pspicts,position="corner")
    pspicts[2].axes.single_axeY.put_mark(0.2,0,label_Y,pspict=pspicts,position="corner")
    pspicts[2].grid.Dx=15
    pspicts[2].grid.Dy=20
    pspicts[2].DrawGraphs(seg)
    pspicts[2].DrawDefaultAxes()
    pspicts[2].DrawDefaultGrid()


    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
