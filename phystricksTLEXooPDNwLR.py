# -*- coding: utf8 -*-
from phystricks import *

def pl_sur_psp(pl,pspict):
    pts=[   Point(  s[0],s[1] ) for s in pl  ]
    pspict.DrawGraphs(pts)

def TLEXooPDNwLR():
    pspicts,figs = IndependentPictures("TLEXooPDNwLR",3)

    for psp in pspicts :
        psp.dilatation(0.7)

    # DS_4A6
    pl=[(9.5, 8.75), (11.0, 10.0), (8.0, 8.75), (12.5, 11.25), (9.0, 10.0), (9.5, 8.75), (12.5, 13.75), (16.5, 16.25), (11.0, 12.5), (17.0, 17.5), (14.5, 15.0), (13.5, 16.25), (11.5, 12.5), (10.0, 11.25)]
    pl_sur_psp(pl,pspicts[0])

    # DS_5A6
    pl=[(7.0, 11.25), (14.0, 13.75), (14.0, 16.25), (13.5, 12.5), (3.5, 10.0), (4.0, 7.5), (16.5, 17.5), (13.5, 12.5), (7.0, 10.0), (7.0, 13.333333333333334), (11.0, 15.0), (3.5, 8.75), (17.0, 18.75), (11.5, 12.5), (11.0, 13.75), (12.5, 11.25), (6.0, 11.666666666666666), (12.0, 12.5), (8.0, 10.0), (17.5, 18.75)]
    pl_sur_psp(pl,pspicts[1])

    # DS_5B6
    pl=[(12.0, 13.333333333333334), (12.0, 11.666666666666666), (11.5, 11.666666666666666), (16.0, 15.0), (10.0, 10.0), (9.5, 13.75), (10.5, 13.333333333333334), (9.0, 10.0), (11.0, 8.75), (8.5, 7.5), (8.0, 11.25), (11.5, 10.0), (7.5, 8.75), (1.5, 8.75), (7.5, 10.0), (13.5, 13.75), (5.5, 7.5), (11.0, 13.75), (9.5, 7.5), (9.0, 11.666666666666666), (7.0, 10.0), (4.0, 10.0), (5.5, 5.0)]
    pl_sur_psp(pl,pspicts[2])

    for psp in pspicts :
        psp.DrawDefaultAxes()
    
    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
