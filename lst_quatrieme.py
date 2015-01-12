#! /usr/bin/python
# -*- coding: utf8 -*-

import sys
import commun
import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"


myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("6_exercices_feuilles_quatrieme")
myRequest.ok_filenames_list.append("9_mental4")
myRequest.ok_filenames_list.append("10_demonstration")
myRequest.ok_filenames_list.append("12_calcul_litteral")
myRequest.ok_filenames_list.append("16_evaluation")
myRequest.ok_filenames_list.append("11_pythagore")
myRequest.ok_filenames_list.append("3_relatifs4")
myRequest.ok_filenames_list.append("0450_choses_finales")
myRequest.ok_filenames_list.append("22_statistiques")
myRequest.ok_filenames_list.append("27_triangles_droites_paralleles")
myRequest.ok_filenames_list.append("25_grands_prop")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("")
myRequest.ok_filenames_list.append("29_ops_frac4")
myRequest.ok_filenames_list.append("28_thales")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")

if "--no-external" in sys.argv :
    myRequest.add_plugin(commun.set_no_useexternal,"after_pytex")
