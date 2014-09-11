#! /usr/bin/sage -python
# -*- coding: utf8 -*-

"""
Pour tester ce fichier :
    rm *.pdf
    rm *.aux
    rm *.pstricks
    et vérifier que externalize de tikz n'est pas mis pour le test.
"""

from phystricks import *
import sys

from phystricksCBLooYAMumJ import CBLooYAMumJ   # Plusieurs dessins
from phystricksCKOooBQtves import CKOooBQtves   # Plusieurs dessins
from phystricksUKTooJhUzKU import UKTooJhUzKU
from phystricksIPAooQliVZD import IPAooQliVZD   # Celui-ci crée trois dessins.
from phystricksRYDooDLpToB import RYDooDLpToB
from phystricksHHOooQUedri import HHOooQUedri
from phystricksSWHooJzpmlM import SWHooJzpmlM       # Cette fonction en lance deux.
from phystricksCNTooDFQFEQ import CNTooDFQFEQ       # Celle-ci aussi
from phystricksWGCXlvC import WGCXlvC
from phystricksLCUooNGZJFk import LCUooNGZJFk
from phystricksKXXooKBoqAY import KXXooKBoqAY
from phystricksDPXooCqCUDl import DPXooCqCUDl
from phystricksSTSooGUprbS import STSooGUprbS
from phystricksJSFooDBSHFo import JSFooDBSHFo
from phystricksVFAooZmuvtW import VFAooZmuvtW
from phystricksSZYooRuSplc import SZYooRuSplc
from phystricksTQDooEgJgPZ import TQDooEgJgPZ
from phystricksMVHooAdkhKq import MVHooAdkhKq
from phystricksRWZooOBMHZ import RWZooOBMHZ
from phystricksLXWooEsxsx import LXWooEsxsx
from phystricksIERooEvNjp import IERooEvNjp
from phystricksTAIooroZRs import TAIooroZRs
from phystricksMTZooSGviQ import MTZooSGviQ
from phystricksMJZoobAMRb import MJZoobAMRb
from phystricksNUWooJepuh import NUWooJepuh
from phystricksHYKooCotyT import HYKooCotyT
from phystricksVGQoojvDGr import VGQoojvDGr
from phystricksSUCoowlFdp import SUCoowlFdp
from phystricksOZXooCVkgQ import OZXooCVkgQ
from phystricksJLrRNbT import JLrRNbT
from phystricksYMslVxg import YMslVxg
from phystricksTCpyyhO import TCpyyhO
from phystricksGJbvyTt import GJbvyTt
from phystricksQGaeERu import QGaeERu
from phystricksQFpJtQc import QFpJtQc
from phystricksOLuvnaY import OLuvnaY
from phystricksIBmsroy import IBmsroy
from phystricksGUEjmmR import GUEjmmR
from phystricksCFjmTFb import CFjmTFb
from phystricksOCFmVDE import OCFmVDE
from phystricksNIGYQHN import NIGYQHN
from phystricksZMGMLvNBa import ZMGMLvNBa
from phystricksSWFywZG import SWFywZG
from phystricksDDRbyQk import DDRbyQk
from phystricksQGRiHbb import QGRiHbb
from phystricksCFFyezr import CFFyezr
from phystricksOKeZlpK import OKeZlpK
from phystricksUZlaYZ import UZlaYZ
from phystricksXMjsBcU import XMjsBcU
from phystricksWTVlzUE import WTVlzUE
from phystricksRHfkPKj import RHfkPKj
from phystricksRZwXiJD import RZwXiJD
from phystricksGTyQVvw import GTyQVvw
from phystricksXDdastq import XDdastq
from phystricksAILoxBg import AILoxBg
from phystricksKYbSnVB import KYbSnVB
from phystricksOZfyDkr import OZfyDkr
from phystricksWPrirwB import WPrirwB
from phystricksEDEYRhQ import EDEYRhQ
from phystricksILauamX import ILauamX
from phystricksEJbcoxO import EJbcoxO
from phystricksGSfDCyx import GSfDCyx
from phystricksRRlBSZg import RRlBSZg
from phystricksFFyFBoe import FFyFBoe
from phystricksJLUTBlD import JLUTBlD
from phystricksQLbEnnx import QLbEnnx
from phystricksAPNeGtp import APNeGtp
from phystricksRLGQTQR import RLGQTQR
from phystricksPUGmLBC import PUGmLBC
from phystricksJXWXdJI import JXWXdJI
from phystricksWYeESAN import WYeESAN
from phystricksYBxSjFS import YBxSjFS
from phystricksEDnzyzS import EDnzyzS
from phystricksYGlrtNX import YGlrtNX
from phystricksDNYAefI import DNYAefI
from phystricksPYYEasw import PYYEasw
from phystricksHMNXfhy import HMNXfhy
from phystricksWGhpCVm import WGhpCVm
from phystricksMUriGyU import MUriGyU
from phystricksUKBImJl import UKBImJl
from phystricksAPYEkIv import APYEkIv
from phystricksALzPUfm import ALzPUfm
from phystricksLTenBUj import LTenBUj
from phystricksMAXkaGz import MAXkaGz
from phystricksYRQOoPE import YRQOoPE
from phystricksONMRllE import ONMRllE
from phystricksMEzTDZC import MEzTDZC
from phystricksXPqLRCF import XPqLRCF
from phystricksXPqLRCF import VXFxyni
from phystricksPXsdjSu import PXsdjSu
from phystricksPXsdjSu import LQGzkvL
from phystricksITlywMb import ITlywMb
from phystricksKMJQWwa import KMJQWwa
from phystricksVDqUhPV import VDqUhPV
from phystricksLSaSLoS import LSaSLoS
from phystricksAVFexUi import AVFexUi
from phystricksBZqEWco import BZqEWco
from phystricksOSQOqJN import OSQOqJN
from phystricksOIHVjmO import OIHVjmO
from phystricksCZAVGrm import CZAVGrm
from phystricksFLnDVHh import FLnDVHh
from phystricksIXtyOnk import IXtyOnk
from phystricksKQluTdN import KQluTdN
from phystricksITZAPPh import ITZAPPh
from phystricksXSMDwcv import XSMDwcv
from phystricksIQnEPpt import IQnEPpt
from phystricksYVZAXhU import YVZAXhU
from phystricksJRVlexw import JRVlexw
from phystricksGCxOEgb import GCxOEgb
from phystricksJHrkjFz import JHrkjFz
from phystricksBIlgjwy import BIlgjwy
from phystricksLOBVHYF import LOBVHYF
from phystricksYORfWSM import YORfWSM
from phystricksVMNerGf import VMNerGf
from phystricksTOcdZDG import TOcdZDG
from phystricksYAaXJqQ import YAaXJqQ
from phystricksfigureWYxZPMW import figureWYxZPMW
from phystricksfigureCFoZCYe import figureCFoZCYe
from phystricksfigureSNpNWPt import figureSNpNWPt
from phystricksfigureZEKOYck import figureZEKOYck
from phystricksfigureMIdFCNN import figureMIdFCNN
from phystricksfigureSIZwqIZ import figureSIZwqIZ
from phystricksfigureEHyIMRQ import figureEHyIMRQ
from phystricksfigureKAzSlQr import figureKAzSlQr
from phystricksfigureSZyxsvp import figureSZyxsvp
from phystricksfigureXCScSiP import figureXCScSiP
from phystricksfigureHYeBZVj import figureHYeBZVj
from phystricksKKEdcAR import KKEdcAR
from phystricksfigureFGgTGJA import figureFGgTGJA
from phystricksfigureHFdjZpb import figureHFdjZpb
from phystricksfigureISQqBVu import figureISQqBVu
from phystricksfigurePQKzIRY import figurePQKzIRY
from phystricksfigureMYeLqLl import figureMYeLqLl
from phystricksfigureDTzvwiz import figureDTzvwiz
from phystricksfigureTJkpHLv import figureTJkpHLv
from phystricksfigureEWDVDTS import figureEWDVDTS
from phystricksfigureXNAufCh import figureXNAufCh
from phystricksfigureQUtOjcm import figureQUtOjcm
from phystricksfigureUERGVgS import figureUERGVgS
from phystricksfigureSCkAAJI import figureSCkAAJI
from phystricksfigureBOuQJyj import figureBOuQJyj
from phystricksfigureVNaHvXi import figureVNaHvXi
from phystricksfigureLEOvqez import figureLEOvqez
from phystricksfigureFNkqWFE import figureFNkqWFE
from phystricksfigureNNgEEzx import figureNNgEEzx
from phystricksfigureXQZwoWu import figureXQZwoWu
from phystricksfigureKHUxoaG import figureKHUxoaG
from phystricksfigureYWEhCkv import figureYWEhCkv
from phystricksJOKJMTD import JOKJMTD
from phystricksfigureWFDTzSN import figureWFDTzSN
from phystricksfigureNPQwFTp import figureNPQwFTp
from phystricksfigureERITfSy import figureERITfSy
from phystricksfigureBCtCTZo import figureBCtCTZo
from phystricksPositionPlansqSltxa import PositionPlansqSltxa
from phystricksPositionPlansTvKvah import PositionPlansTvKvah
from phystricksPositionRelativexpwkEJ import PositionRelativexpwkEJ
from phystricksExoTrigTrIpPW import ExoTrigTrIpPW
from phystricksExoVectoFRPXxB import ExoVectoFRPXxB

#from phystricksTracerUn import TracerUn
#from phystricksGrapheunsurunmoinsx import Grapheunsurunmoinsx
#from phystricksExerciceGraphes import ExerciceGraphes
#from phystricksExerciceGraphesbis import ExerciceGraphesbis
#from phystricksExoCUd import ExoCUd
#from phystricksUnSurxInt import UnSurxInt
#from phystricksAireParabole import AireParabole
#from phystricksPartieEntiere import PartieEntiere
#from phystricksMantisse import Mantisse
#from phystricksDS2010ExoGraph import DS2010ExoGraph
#from phystricksDS2010bisExoGraph import DS2010bisExoGraph
#from phystricksSolsEqDiffSin import SolsEqDiffSin
#from phystricksSolsSinpA import SolsSinpA
#from phystricksTrajs import Trajs

from phystricksEvZZys import EvZZys
from phystricksBpCNVm import BpCNVm
#from phystricksNotesSVT import NotesSVT
from phystricksHistoAutomobile import HistoAutomobile
from phystricksHistoTdkccB import HistoTdkccB
from phystricksHistoPySeT import HistoPySeT
from phystricksHistoAgeFrance import HistoAgeFrance
from phystricksHistoAgeKenya import HistoAgeKenya
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
from phystricksGrapheVarndvdQM import GrapheVarndvdQM
from phystricksFoncConstFdDkhW import FoncConstFdDkhW
from phystricksGrapheVarREGMqx import GrapheVarREGMqx
from phystricksFnAffineipcEQf import FnAffineipcEQf
from phystricksMinMaxKNRdOd import MinMaxKNRdOd
from phystricksCubeLFZuiW import CubeLFZuiW
from phystricksDesSectionseVPNeL import DesSectionseVPNeL
from phystricksIllusionNHwEtp import IllusionNHwEtp
from phystricksLignesCubeshBfjxk import LignesCubeshBfjxk
from phystricksCylindresxKDOdy import CylindresxKDOdy
from phystricksFaussePerspectivewAwxAJ import FaussePerspectivewAwxAJ
from phystricksCubeLigneTriangleHFMrVU import CubeLigneTriangleHFMrVU
from phystricksSurfaceCubeXlLEEy import SurfaceCubeXlLEEy
from phystricksDansRectangleGPEkJc import DansRectangleGPEkJc
from phystricksPrismeCQlZKY import PrismeCQlZKY
from phystricksIsoceleVdviOE import IsoceleVdviOE
from phystricksPerpSegqrbMBZ import PerpSegqrbMBZ
from phystricksPositionsDroitesbnYIsH import PositionsDroitesbnYIsH
from phystricksCorSSTXPQVjn import CorSSTXPQVjn
from phystricksGraphInterfQVfSf import GraphInterfQVfSf
from phystricksParaboleResumeHNiyfR import ParaboleResumeHNiyfR
from phystricksParaboleResumeSzaWaG import ParaboleResumeSzaWaG
from phystricksSimulBinNWxfTN import SimulBinNWxfTN
from phystricksFnInterrobgepC import FnInterrobgepC
from phystricksRouletteACaVAA import RouletteACaVAA
from phystricksPetiteBinomialelzbdWl import PetiteBinomialelzbdWl
from phystricksGrandeBinomialeIyWAIh import GrandeBinomialeIyWAIh
from phystricksExoBinomialeNyQLYI import ExoBinomialeNyQLYI
from phystricksRectanglegHuBZs import RectanglegHuBZs
from phystricksThaleszlOKVq import ThaleszlOKVq
from phystricksExoTranslationPNjoHk import ExoTranslationPNjoHk
from phystricksDefVecteurAXDDGP import DefVecteurAXDDGP
from phystricksVectoParallItzteT import VectoParallItzteT
from phystricksVectoParallelgjDlmD import VectoParallelgjDlmD
from phystricksChaslesGTRtKR import ChaslesGTRtKR
from phystricksVectoMilieuNuWgHW import VectoMilieuNuWgHW
from phystricksExoVectoPJGrRF import ExoVectoPJGrRF
from phystricksfigureASkECWS import figureASkECWS
from phystricksfigureCSIQETx import figureCSIQETx
from phystricksfigureTFaRFVd import figureTFaRFVd
from phystricksfigureITVTofz import figureITVTofz
from phystricksfigureNAKnjxQ import figureNAKnjxQ
from phystricksfigureAEcZqpP import figureAEcZqpP
from phystricksEGDFJAT import EGDFJAT
from phystricksAHAbqhj import AHAbqhj
from phystricksWRXbDCo import WRXbDCo
from phystricksGRRhrJe import GRRhrJe
from phystricksAZKoIsL import AZKoIsL
from phystricksOWGRRSC import OWGRRSC
from phystricksZQfGNsD import ZQfGNsD
from phystricksIRHrmQQ import IRHrmQQ
from phystricksKGOAveW import KGOAveW
from phystricksIDqyzXM import IDqyzXM
from phystricksETfnbsh import ETfnbsh
from phystricksENQhxmG import ENQhxmG
from phystricksKDtwIJf import KDtwIJf
from phystricksFWyrYhJ import FWyrYhJ
from phystricksBZRzIsR import BZRzIsR
from phystricksITzxISE import ITzxISE
from phystricksEIxhcRb import EIxhcRb
from phystricksLZDNqtV import LZDNqtV
from phystricksRVZNtGK import RVZNtGK
from phystricksTWGooMalxLa import TWGooMalxLa

# À surveiller :
from phystricksSurfacesCubesclGZD import SurfacesCubesclGZD


def AllFigures(figures_list):
    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"Un soupçon de mathématiques")
    tests.generate()
    tests.summary()

# Les fonctions suivantes sont supprimées (12 septembre 2013)
#DS2010bisExoGraph, ExoCUd,DS2010ExoGraph,
# Les fonctions suivantes sont supprimées (27 août 2014)
#   from phystricksExGrapheOcxXii import ExGrapheOcxXii
#   from phystricksSecondDeg import SecondDeg
# from phystricksExoGraphIneqPgErDr import ExoGraphIneqPgErDr
# from phystricksOHfdEZt import OHfdEZt
# from phystricksUEqUrvi import UEqUrvi
# from phystricksDZmbmzZ import DZmbmzZ
# from phystricksLNfaWPF import LNfaWPF
# from phystricksFPIkJJx import FPIkJJx
# from phystricksOKTXHoc import OKTXHoc
# from phystricksJLUTBlD import JWNtVIR
# from phystricksAUHmNET import AUHmNET

figures_list=[]
figures_list.append(EvZZys)
figures_list.append(BpCNVm)
figures_list.append(HistoAutomobile)
figures_list.append(HistoTdkccB)
figures_list.append(HistoPySeT)
figures_list.append(HistoAgeFrance)
figures_list.append(HistoAgeKenya)
figures_list.append(EffectifsCumulwfqAhj)
figures_list.append(SurfaceTriangletcNPPE)
figures_list.append(ParabolevQzhjq)
figures_list.append(bDdpfh)
figures_list.append(ParaboleiLbviP)
figures_list.append(ParaboleMCLCbG)
figures_list.append(ParaboleHautMLbPQF)
figures_list.append(ParaboleBasfKtFCN)
figures_list.append(ParabolezBeHFl)
figures_list.append(ParabolezmMGdN)
figures_list.append(ParaboleUneSolPktmCR)
figures_list.append(ParaboleHautjOEAzn)
figures_list.append(ParaboleBasDqAAua)
figures_list.append(ParaboleUniqueHautviflbY)
figures_list.append(ParaboleUniqueBaskGdqda)
figures_list.append(MathCeilwCXIJZ)
figures_list.append(ReperexjVyii)
figures_list.append(PythagoreeBqLDU)
figures_list.append(ParaboleoytUKk)
figures_list.append(ParabolesoDGyNW)
figures_list.append(GrapheAffinHqXJGx)
figures_list.append(ExoIntersectionCourbenzIxXd)
figures_list.append(FCarreQFhsWz)
figures_list.append(ExCarrexvfvre)
figures_list.append(ExResolutionOSiaMS)
figures_list.append(ExEquationIntersectioniSHPTw)
figures_list.append(ExIneqOcAWMq)
figures_list.append(ExIneqfgZWStde)
figures_list.append(ExVariationRXTkoc)
figures_list.append(GrapheVarndvdQM)
figures_list.append(FoncConstFdDkhW)
figures_list.append(GrapheVarREGMqx)
figures_list.append(FnAffineipcEQf)
figures_list.append(MinMaxKNRdOd)
figures_list.append(ParabolesfTKFw)
figures_list.append(CubeLFZuiW)
figures_list.append(DesSectionseVPNeL)
figures_list.append(LectureGraphnrkEEM)
figures_list.append(PasFonctionYoQfSu)
figures_list.append(IllusionNHwEtp)
figures_list.append(LignesCubeshBfjxk)
figures_list.append(FaussePerspectivewAwxAJ)
figures_list.append(CubeLigneTriangleHFMrVU)
figures_list.append(SurfaceCubeXlLEEy)
figures_list.append(DansRectangleGPEkJc)
figures_list.append(PrismeCQlZKY)
figures_list.append(IsoceleVdviOE)
figures_list.append(PerpSegqrbMBZ)
figures_list.append(PositionsDroitesbnYIsH)
figures_list.append(CorSSTXPQVjn)
figures_list.append(GraphInterfQVfSf)
figures_list.append(ParaboleResumeHNiyfR)
figures_list.append(ParaboleResumeSzaWaG)
figures_list.append(SimulBinNWxfTN)
figures_list.append(FnInterrobgepC)
figures_list.append(RouletteACaVAA)
figures_list.append(PetiteBinomialelzbdWl)
figures_list.append(GrandeBinomialeIyWAIh)
figures_list.append(ExoBinomialeNyQLYI)
figures_list.append(RectanglegHuBZs)
figures_list.append(ThaleszlOKVq)
figures_list.append(DefVecteurAXDDGP)
figures_list.append(VectoParallItzteT)
figures_list.append(VectoParallelgjDlmD)
figures_list.append(ChaslesGTRtKR)
figures_list.append(VectoMilieuNuWgHW)
figures_list.append(ExoVectoFRPXxB)
figures_list.append(ExoVectoPJGrRF)
figures_list.append(ExoTrigTrIpPW)
figures_list.append(PositionRelativexpwkEJ)
figures_list.append(PositionPlansTvKvah)
figures_list.append(PositionPlansqSltxa)
figures_list.append(figureBCtCTZo)
figures_list.append(figureASkECWS)
figures_list.append(figureCSIQETx)
figures_list.append(figureTFaRFVd)
figures_list.append(figureERITfSy)
figures_list.append(figureNPQwFTp)
figures_list.append(figureITVTofz)
figures_list.append(figureNAKnjxQ)
figures_list.append(figureWFDTzSN)
figures_list.append(JOKJMTD)
figures_list.append(figureYWEhCkv)
figures_list.append(figureAEcZqpP)
figures_list.append(ExoTranslationPNjoHk)
figures_list.append(figureKHUxoaG)
figures_list.append(figureXQZwoWu)
figures_list.append(CylindresxKDOdy)
figures_list.append(figureNNgEEzx)
figures_list.append(figureFNkqWFE)
figures_list.append(figureLEOvqez)
figures_list.append(figureVNaHvXi)
figures_list.append(figureBOuQJyj)
figures_list.append(figureSCkAAJI)
figures_list.append(figureUERGVgS)
figures_list.append(figureQUtOjcm)
figures_list.append(figureXNAufCh)
figures_list.append(figureEWDVDTS)
figures_list.append(figureTJkpHLv)
figures_list.append(figureDTzvwiz)
figures_list.append(figureMYeLqLl)
figures_list.append(figurePQKzIRY)
figures_list.append(figureISQqBVu)
figures_list.append(figureHFdjZpb)
figures_list.append(figureFGgTGJA)
figures_list.append(KKEdcAR)
figures_list.append(figureXCScSiP)
figures_list.append(figureSZyxsvp)
figures_list.append(figureHYeBZVj)
figures_list.append(figureKAzSlQr)
figures_list.append(figureEHyIMRQ)
figures_list.append(figureSIZwqIZ)
figures_list.append(figureMIdFCNN)
figures_list.append(figureZEKOYck)
figures_list.append(figureSNpNWPt)
figures_list.append(figureCFoZCYe)
figures_list.append(figureWYxZPMW)
figures_list.append(YAaXJqQ)
figures_list.append(TOcdZDG)
figures_list.append(VMNerGf)
figures_list.append(YORfWSM)
figures_list.append(LOBVHYF)
figures_list.append(BIlgjwy)
figures_list.append(JHrkjFz)
figures_list.append(GCxOEgb)
figures_list.append(JRVlexw)
figures_list.append(YVZAXhU)
figures_list.append(IQnEPpt)
figures_list.append(XSMDwcv)
figures_list.append(ITZAPPh)
figures_list.append(KQluTdN)
figures_list.append(IXtyOnk)
figures_list.append(FLnDVHh)
figures_list.append(CZAVGrm)
figures_list.append(OIHVjmO)
figures_list.append(OSQOqJN)
figures_list.append(BZqEWco)
figures_list.append(AVFexUi)
figures_list.append(LSaSLoS)
figures_list.append(VDqUhPV)
figures_list.append(KMJQWwa)
figures_list.append(ITlywMb)
figures_list.append(EGDFJAT)
figures_list.append(AHAbqhj)
figures_list.append(WRXbDCo)
figures_list.append(GRRhrJe)
figures_list.append(AZKoIsL)
figures_list.append(OWGRRSC)
figures_list.append(ZQfGNsD)
figures_list.append(IRHrmQQ)
figures_list.append(KGOAveW)
figures_list.append(PXsdjSu)
figures_list.append(XPqLRCF)
figures_list.append(MEzTDZC)
figures_list.append(ONMRllE)
figures_list.append(IDqyzXM)
figures_list.append(ETfnbsh)
figures_list.append(ENQhxmG)
figures_list.append(YRQOoPE)
figures_list.append(KDtwIJf)
figures_list.append(MAXkaGz)
figures_list.append(LTenBUj)
figures_list.append(ALzPUfm)
figures_list.append(LQGzkvL)
figures_list.append(APYEkIv)
figures_list.append(UKBImJl)
figures_list.append(MUriGyU)
figures_list.append(WGhpCVm)
figures_list.append(HMNXfhy)
figures_list.append(PYYEasw)
figures_list.append(DNYAefI)
figures_list.append(FWyrYhJ)
figures_list.append(YGlrtNX)
figures_list.append(EDnzyzS)
figures_list.append(BZRzIsR)
figures_list.append(VXFxyni)
figures_list.append(YBxSjFS)
figures_list.append(ITzxISE)
figures_list.append(RLGQTQR)
figures_list.append(WYeESAN)
figures_list.append(EIxhcRb)
figures_list.append(JXWXdJI)
figures_list.append(PUGmLBC)
figures_list.append(LZDNqtV)
figures_list.append(APNeGtp)
figures_list.append(QLbEnnx)
figures_list.append(JLUTBlD)
figures_list.append(FFyFBoe)
figures_list.append(RRlBSZg)
figures_list.append(GSfDCyx)
figures_list.append(EJbcoxO)
figures_list.append(ILauamX)
figures_list.append(EDEYRhQ)
figures_list.append(WPrirwB)
figures_list.append(OZfyDkr)
figures_list.append(KYbSnVB)
figures_list.append(AILoxBg)
figures_list.append(XDdastq)
figures_list.append(GTyQVvw)
figures_list.append(RZwXiJD)
figures_list.append(RHfkPKj)
figures_list.append(WTVlzUE)
figures_list.append(XMjsBcU)
figures_list.append(UZlaYZ)
figures_list.append(OKeZlpK)
figures_list.append(RVZNtGK)
figures_list.append(CFFyezr)
figures_list.append(QGRiHbb)
figures_list.append(DDRbyQk)
figures_list.append(SWFywZG)
figures_list.append(ZMGMLvNBa)
figures_list.append(NIGYQHN)
figures_list.append(OCFmVDE)
figures_list.append(CFjmTFb)
figures_list.append(GUEjmmR)
figures_list.append(IBmsroy)
figures_list.append(OLuvnaY)
figures_list.append(QFpJtQc)
figures_list.append(QGaeERu)
figures_list.append(GJbvyTt)
figures_list.append(TCpyyhO)
figures_list.append(YMslVxg)
figures_list.append(JLrRNbT)
figures_list.append(OZXooCVkgQ)
figures_list.append(SUCoowlFdp)
figures_list.append(VGQoojvDGr)
figures_list.append(HYKooCotyT)
figures_list.append(NUWooJepuh)
figures_list.append(MJZoobAMRb)
figures_list.append(MTZooSGviQ)
figures_list.append(TAIooroZRs)
figures_list.append(IERooEvNjp)
figures_list.append(LXWooEsxsx)
figures_list.append(RWZooOBMHZ)
figures_list.append(MVHooAdkhKq)
figures_list.append(TQDooEgJgPZ)
figures_list.append(JSFooDBSHFo)
figures_list.append(STSooGUprbS)
figures_list.append(DPXooCqCUDl)
figures_list.append(SZYooRuSplc)
figures_list.append(VFAooZmuvtW)
figures_list.append(WGCXlvC)
figures_list.append(TWGooMalxLa)
figures_list.append(LCUooNGZJFk)
figures_list.append(KXXooKBoqAY)
figures_list.append(SurfacesCubesclGZD)
figures_list.append(SWHooJzpmlM)
figures_list.append(RYDooDLpToB)
figures_list.append(IPAooQliVZD)
figures_list.append(UKTooJhUzKU)
figures_list.append(CKOooBQtves)
"""
figures_list.append(<++>)
figures_list.append(<++>)
figures_list.append(<++>)
figures_list.append(<++>)
figures_list.append(<++>)
"""


#figures_list=[]

for k in sys.argv:
    s=[]
    fun=k.replace("phystricks","").replace(".py","")
    print fun
    if fun in globals().keys():
        print "ok"
        s.append(globals()[fun])

if s:
    figures_list=s

if __name__=="__main__":
    if "--all" not in sys.argv :
        figures_list=figures_list[-1:]

    AllFigures(figures_list)
