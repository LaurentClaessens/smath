# -*- coding: utf8 -*-
from phystricks import *

import phystricksCommons

def LRWooCalQsT():
    pspict,fig = SinglePicture("LRWooCalQsT")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    #moustaches.append(Moustache(5.82,9.05,11.42,13.52,18.05,h=0.5,delta_y=0.75))    # DS1
    #moustaches.append(Moustache(4.30,13.06,16.49,17.59,19.40,h=0.5,delta_y=0.75))   # DS2
    #moustaches.append(Moustache(3.17,9.81,13.15,14.80,16.65,h=0.5,delta_y=0.75))    # DS3
    #moustaches.append(Moustache(8.55,12.10,14.67,16.19,20.00,h=0.5,delta_y=0.75))   # DS4
    #moustaches.append(Moustache(4.20,8.63,11.88,14.65,16.10,h=0.5,delta_y=0.75))    # DS5
    #moustaches.append(Moustache(8.00,9.50,11.25,13.55,17.00,h=0.5,delta_y=0.75))    # DS6

    moustaches.append(BoxDiagram([9.016666666666666, 12.816666666666668, 6.2, 11.416666666666666, 9.866666666666665, 11.416666666666666, 11.066666666666668, 5.816666666666667, 13.566666666666668, 18.05, 11.816666666666666, 14.166666666666666, 14.7, 7.566666666666667, 15.25, 12.566666666666666, 13.333333333333332, 9.2, 6.083333333333333],h=0.5,delta_y=0.75))     # DS1
    moustaches.append(BoxDiagram([11.65, 15.419999999999998, 10.53, 12.47, 16.27, 15.36, 17.18, 16.72, 4.3, 18.26, 19.07, 16.970000000000002, 19.4, 18.39, 14.580000000000002, 16.939999999999998, 17.45, 17.7, 13.790000000000001, 6.57],h=0.5,delta_y=0.75))     #DS2
    moustaches.append(BoxDiagram([13.873333333333337, 14.800000000000002, 12.793333333333337, 15.84666666666667, 13.58666666666667, 14.833333333333334, 14.666666666666671, 3.166666666666668, 12.720000000000002, 17.880000000000003, 12.413333333333336, 16.060000000000006, 11.380000000000003, 9.173333333333336, 13.500000000000002, 16.64666666666667, 9.84666666666667, 3.8800000000000012, 6.033333333333334],h=0.5,delta_y=0.75))     # DS3
    moustaches.append(BoxDiagram([11.916666666666666, 12.916666666666668, 12.416666666666666, 12.183333333333334, 16.55, 14.666666666666668, 14.9, 18.9, 14.866666666666669, 20.0, 15.783333333333335, 9.266666666666667, 16.166666666666664, 16.233333333333334, 12.816666666666668, 8.546666666666667, 11.893333333333333],h=0.5,delta_y=0.75))     # DS4
    moustaches.append(BoxDiagram([5.55, 9.3, 12.200000000000001, 12.75, 4.199999999999999, 12.425, 9.375, 11.875, 4.8, 15.8, 16.1, 11.875, 15.9, 10.9, 9.95, 15.975, 15.525, 13.575, 8.075000000000001, 5.85],h=0.5,delta_y=0.75)) # DS5
    moustaches.append(BoxDiagram([9.500000000000002, 11.000000000000002, 8.000000000000002, 12.500000000000002, 9.000000000000002, 9.500000000000002, 12.500000000000002, 16.500000000000004, 11.000000000000002, 17.000000000000004, 14.500000000000002, 13.500000000000002, 11.500000000000002, 10.000000000000002],h=0.5,delta_y=0.75))   # DS6


    phystricksCommons.DS_statistics(moustaches,pspict)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
