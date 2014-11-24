# -*- coding: utf8 -*-
from phystricks import *

import phystricksCommons

def LRWooCalQsT():
    pspict,fig = SinglePicture("LRWooCalQsT")

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(5.82,9.05,11.42,13.52,18.05,h=0.5,delta_y=0.75))    # DS1
    moustaches.append(Moustache(4.30,13.06,16.49,17.59,19.40,h=0.5,delta_y=0.75))   # DS2
    moustaches.append(Moustache(3.17,9.81,13.15,14.80,16.65,h=0.5,delta_y=0.75))    # DS3

    phystricksCommons.DS_statistics(moustaches,pspict)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
