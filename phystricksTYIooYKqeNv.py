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
    JNGEooISdbXx()