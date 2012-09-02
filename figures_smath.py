#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from phystricks import *
import sys

from phystricksEvZZys import EvZZys

figures_list=[ EvZZys            ]


def AllFigures():
    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"soupçon de mathématiques")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        ProjPoly()
