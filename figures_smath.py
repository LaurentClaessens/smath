#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from phystricks import *
import sys

from phystricksTracerUn import TracerUn
from phystricksExerciceGraphes import ExerciceGraphes
from phystricksExerciceGraphesbis import ExerciceGraphesbis
from phystricksGrapheunsurunmoinsx import Grapheunsurunmoinsx
from phystricksExoCUd import ExoCUd
from phystricksUnSurxInt import UnSurxInt
from phystricksAireParabole import AireParabole
from phystricksPartieEntiere import PartieEntiere
from phystricksMantisse import Mantisse
from phystricksDS2010ExoGraph import DS2010ExoGraph
from phystricksDS2010bisExoGraph import DS2010bisExoGraph
from phystricksSolsEqDiffSin import SolsEqDiffSin
from phystricksSolsSinpA import SolsSinpA
from phystricksTrajs import Trajs

from phystricksEvZZys import EvZZys
from phystricksBpCNVm import BpCNVm

figures_list=[DS2010bisExoGraph, ExoCUd,DS2010ExoGraph,SolsEqDiffSin,
            Grapheunsurunmoinsx, TracerUn, ExerciceGraphes,SolsSinpA,Trajs,
        	ExerciceGraphesbis, UnSurxInt, AireParabole, PartieEntiere, Mantisse,
            EvZZys,BpCNVm  ]

def AllFigures():
    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"soupçon de mathématiques")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        BpCNVm()
