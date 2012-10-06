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
#from phystricksNotesSVT import NotesSVT
from phystricksHistoAutomobile import HistoAutomobile
from phystricksHistoTdkccB import HistoTdkccB
from phystricksHistoPySeT import HistoPySeT
from phystricksHistoAgeFrance import HistoAgeFrance
from phystricksHistoAgeKenya import HistoAgeKenya
from phystricksSecondDeg import SecondDeg
from phystricksParabolesfTKFw import ParabolesfTKFw
from phystricksEffectifsCumulwfqAhj import EffectifsCumulwfqAhj
from phystricksSurfaceTriangletcNPPE import SurfaceTriangletcNPPE
from phystricksLectureGraphnrkEEM import LectureGraphnrkEEM
from phystricksParaboleMCLCbG import ParaboleMCLCbG
from phystricksbDdpfh import bDdpfh
from phystricksParabolevQzhjq import ParabolevQzhjq
from phystricksParaboleiLbviP import ParaboleiLbviP
from phystricksParaboleHautMLbPQF import ParaboleHautMLbPQF
from phystricksParaboleBasfKtFCN import ParaboleBasfKtFCN
from phystricksParabolezBeHFl import ParabolezBeHFl
from phystricksParabolezmMGdN import ParabolezmMGdN
from phystricksParaboleUneSolPktmCR import ParaboleUneSolPktmCR
from phystricksParaboleHautjOEAzn import ParaboleHautjOEAzn
from phystricksParaboleBasDqAAua import ParaboleBasDqAAua
from phystricksParaboleUniqueHautviflbY import ParaboleUniqueHautviflbY
from phystricksParaboleUniqueBaskGdqda import ParaboleUniqueBaskGdqda
from phystricksMathCeilwCXIJZ import MathCeilwCXIJZ
from phystricksReperexjVyii import ReperexjVyii
from phystricksPythagoreeBqLDU import PythagoreeBqLDU
from phystricksParaboleoytUKk import ParaboleoytUKk
from phystricksParabolesoDGyNW import ParabolesoDGyNW
from phystricksExGrapheOcxXii import ExGrapheOcxXii
from phystricksPasFonctionYoQfSu import PasFonctionYoQfSu
from phystricksGrapheAffinHqXJGx import GrapheAffinHqXJGx
from phystricksExoIntersectionCourbenzIxXd import ExoIntersectionCourbenzIxXd
from phystricksFCarreQFhsWz import FCarreQFhsWz
from phystricksExCarrexvfvre import ExCarrexvfvre
from phystricksExResolutionOSiaMS import ExResolutionOSiaMS
from phystricksExEquationIntersectioniSHPTw import ExEquationIntersectioniSHPTw
from phystricksExIneqOcAWMq import ExIneqOcAWMq
from phystricksExIneqfgZWStde import ExIneqfgZWStde
from phystricksExVariationRXTkoc import ExVariationRXTkoc
from phystricksExoGraphIneqPgErDr import ExoGraphIneqPgErDr
from phystricksExVarGraphiqueyhHpqn import ExVarGraphiqueyhHpqn
from phystricksGrapheVarndvdQM import GrapheVarndvdQM
from phystricksFoncConstFdDkhW import FoncConstFdDkhW
from phystricksGrapheVarREGMqx import GrapheVarREGMqx
from phystricksFnAffineipcEQf import FnAffineipcEQf
from phystricksMinMaxKNRdOd import MinMaxKNRdOd
from phystricksCubeLFZuiW import CubeLFZuiW
from phystricksDesSectionseVPNeL import DesSectionseVPNeL
from phystricksIllusionNHwEtp import IllusionNHwEtp
from phystricksLignesCubeshBfjxk import LignesCubeshBfjxk
from phystricksSurfacesCubesclGZD import SurfacesCubesclGZD

def AllFigures(figures_list):
    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"Soupçon de mathématiques")
    tests.generate()
    tests.summary()

figures_list=[DS2010bisExoGraph, ExoCUd,DS2010ExoGraph,SolsEqDiffSin, Grapheunsurunmoinsx, TracerUn, ExerciceGraphes,SolsSinpA,Trajs, ExerciceGraphesbis,
    UnSurxInt, AireParabole, PartieEntiere, Mantisse, EvZZys,BpCNVm,HistoAutomobile,HistoTdkccB,HistoPySeT, HistoAgeFrance,HistoAgeKenya,
    EffectifsCumulwfqAhj,SurfaceTriangletcNPPE,ParabolevQzhjq,bDdpfh,ParaboleiLbviP,ParaboleMCLCbG,ParaboleHautMLbPQF,
    ParaboleBasfKtFCN,ParabolezBeHFl,ParabolezmMGdN,ParaboleUneSolPktmCR,ParaboleHautjOEAzn,ParaboleBasDqAAua,ParaboleUniqueHautviflbY,
    ParaboleUniqueBaskGdqda, MathCeilwCXIJZ,ReperexjVyii,PythagoreeBqLDU,ParaboleoytUKk,ParabolesoDGyNW,SecondDeg,ExGrapheOcxXii,
    GrapheAffinHqXJGx,ExoIntersectionCourbenzIxXd,FCarreQFhsWz,ExCarrexvfvre,ExResolutionOSiaMS,ExEquationIntersectioniSHPTw,ExIneqOcAWMq,
    ExIneqfgZWStde,ExVariationRXTkoc,ExoGraphIneqPgErDr,ExVarGraphiqueyhHpqn,GrapheVarndvdQM,FoncConstFdDkhW,GrapheVarREGMqx,FnAffineipcEQf,MinMaxKNRdOd,
    ParabolesfTKFw,CubeLFZuiW,DesSectionseVPNeL,LectureGraphnrkEEM,PasFonctionYoQfSu,IllusionNHwEtp,LignesCubeshBfjxk,SurfacesCubesclGZD
    ]

if __name__=="__main__":
    if "--all" not in sys.argv :
        figures_list=figures_list[-1:]

    AllFigures(figures_list)
