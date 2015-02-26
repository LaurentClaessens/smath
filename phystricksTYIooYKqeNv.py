# -*- coding: utf8 -*-
from phystricks import *

import phystricksCommons

def CXWooOMPOQT():
    # 5A
    pspict,fig = SinglePicture("CXWooOMPOQT")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(7.90,10.20,14.45,16.70,20.00,h=0.5,delta_y=0.75))   # DS1
    moustaches.append(Moustache(5.10,8.75,10.87,16.29,20.00,h=0.5,delta_y=0.75))    # DS2
    moustaches.append(Moustache(5.88,10.36,14.41,16.75,20.00,h=0.5,delta_y=0.75))   # DS3
    moustaches.append(Moustache(4.42,9.80,12.57,16.64,20.00,h=0.5,delta_y=0.75))    # DS4
    moustaches.append(Moustache(8.00,12.60,14.00,18.70,20.00,h=0.5,delta_y=0.75))   # DS5
    moustaches.append(Moustache(3.50,7.00,11.00,13.28,17.50,h=0.5,delta_y=0.75))    # DS6

    phystricksCommons.DS_statistics(moustaches,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def PJQooTWPTXV():
    # 5B
    pspict,fig = SinglePicture("PJQooTWPTXV")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(6.00,8.99,11.50,14.37,20.00,h=0.5,delta_y=0.75))    # DS1
    moustaches.append(Moustache(4.93,7.71,11.85,14.03,16.48,h=0.5,delta_y=0.75))    # DS2
    moustaches.append(Moustache(4.90,7.38,10.35,13.36,17.09,h=0.5,delta_y=0.75))    # DS3
    moustaches.append(Moustache(1.50,7.57,10.23,13.12,16.03,h=0.5,delta_y=0.75))    # DS4
    moustaches.append(Moustache(4.50,6.50,9.25,14.03,15.50,h=0.5,delta_y=0.75))     # DS5
    moustaches.append(Moustache(1.50,7.50,9.50,11.40,16.00,h=0.5,delta_y=0.75))     # DS6

    phystricksCommons.DS_statistics(moustaches,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


def JNGEooISdbXx():
    # 5AB mélangés
    pspict,fig = SinglePicture("JNGEooISdbXx")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(6.00,10.10,12.10,16.30,20.00,h=0.5,delta_y=0.75))   # DS1
    moustaches.append(Moustache(4.93,8.08,11.45,15.20,20.00,h=0.5,delta_y=0.75))    # DS2

    phystricksCommons.DS_statistics(moustaches,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def TYIooYKqeNv():
    PJQooTWPTXV()
    CXWooOMPOQT()
    #JNGEooISdbXx()
