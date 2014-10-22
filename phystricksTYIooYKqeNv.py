# -*- coding: utf8 -*-
from phystricks import *

import phystricksCommons

def PJQooTWPTXV():
    pspict,fig = SinglePicture("PJQooTWPTXV")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(6.00,8.99,11.50,14.37,20.00,h=0.5,delta_y=0.75))    #DS1

    phystricksCommons.DS_statistics(moustaches,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def CXWooOMPOQT():
    pspict,fig = SinglePicture("CXWooOMPOQT")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(7.90,10.20,14.45,16.70,20.00,h=0.5,delta_y=0.75))   # DS1

    phystricksCommons.DS_statistics(moustaches,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def JNGEooISdbXx():
    # Les graphes des deux cinquièmes mélangées.
    pspict,fig = SinglePicture("JNGEooISdbXx")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(6.00,10.10,12.10,16.30,20.00,h=0.5,delta_y=0.75))   # DS1
    moustaches.append(Moustache(4.35,7.45,11.59,15.49,20.00,h=0.5,delta_y=0.75))

    phystricksCommons.DS_statistics(moustaches,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def TYIooYKqeNv():
    #PJQooTWPTXV()
    #CXWooOMPOQT()
    JNGEooISdbXx()

