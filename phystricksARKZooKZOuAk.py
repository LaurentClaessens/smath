# -*- coding: utf8 -*-

from phystricks import *
import commun

def ARKZooKZOuAk():
    pspicts,figs = IndependentPictures("ARKZooKZOuAk",4)

    pspicts[0].dilatation(0.6)

    pspicts[1].dilatation_X(0.7)
    pspicts[1].dilatation_Y(0.07)

    pspicts[2].dilatation_X(0.2)
    pspicts[2].dilatation_Y(0.1)

    pspicts[3].dilatation_X(1)
    pspicts[3].dilatation_Y(0.3)
    
    A=commun.Situation(name="ARKZooKZOuAkconvprix", p1= "prix en euros",p2="prix en wut", pts=[ (1,1.5),(2,3),(3,4.5),(4,6)  ]   )
    A.write_the_file()

    pspicts[1].Mx_acceptable_BB=120
    
    B=commun.Situation(name="ARKZooKZOuAkfar", p1= "Température en Fahrenheit",p2="Témpérature en Celsius", pts=[ (14,-10),(32,0),(41,5),(59,15),(95,35)  ]   )
    B.write_the_file()

    C=commun.Situation(name="ARKZooKZOuAkmilm", p1= "distance en mile marin",p2="distance en \si{\kilo\meter}", pts=[ (0,0),(5,9.26),(10,18.52),(15,27.78)  ]   )
    C.write_the_file()

    D=commun.Situation(name="ARKZooKZOuAkctlibre", p1= "Temps de chute libre (\si{\second})",p2="Hauteur parcourue (\si{\meter})", pts=[ (0,0),(0.2,0.19),(0.5,1.22),(0.7,2.4), (1,4.9),(1.2,7),(1.5,11,03) ]   )
    D.write_the_file()

    #<++>=commun.Situation(name="<++>", p1= "<++>",p2="<++>", pts=[ (<++>,<++>),(<++>,<++>),(<++>,<++>),(<++>,<++>)  ]   )
    #<++>.write_the_file()

    pspicts[0].DrawGraphs(A.points_list())
    pspicts[1].DrawGraphs(B.points_list())
    pspicts[2].DrawGraphs(C.points_list())
    pspicts[3].DrawGraphs(D.points_list())


    for psp in pspicts:
        psp.axes.do_my_enlarge=False
        psp.axes.do_mx_enlarge=False

    pspicts[0].DrawDefaultGrid()
    pspicts[0].axes.do_My_enlarge=False
    pspicts[0].DrawDefaultAxes()


    pspicts[1].grid.Dx=20
    pspicts[1].grid.Dy=10
    pspicts[1].DrawDefaultGrid()
    pspicts[1].axes.single_axeX.Dx=20
    pspicts[1].axes.single_axeY.Dx=10
    pspicts[1].DrawDefaultAxes()

    pspicts[2].grid.Dx=5
    pspicts[2].grid.Dy=5
    pspicts[2].DrawDefaultGrid()
    pspicts[2].axes.single_axeX.Dx=5
    pspicts[2].axes.single_axeY.Dx=5
    pspicts[2].axes.do_My_enlarge=False
    pspicts[2].DrawDefaultAxes()

    pspicts[3].grid.Dx=1
    pspicts[3].grid.Dy=2
    pspicts[3].DrawDefaultGrid()
    pspicts[3].single_axeX.Dx=1
    pspicts[3].single_axeY.Dx=2
    pspicts[3].axes.do_My_enlarge=False
    pspicts[3].DrawDefaultAxes()

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
