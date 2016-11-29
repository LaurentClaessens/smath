#! /usr/bin/python
# -*- coding: utf8 -*-

import sys
import commun
import latexparser
import latexparser.PytexTools

myRequest = latexparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"


myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("proportions")
myRequest.ok_filenames_list.append("parabole")
myRequest.ok_filenames_list.append("Binomiale")
myRequest.ok_filenames_list.append("evolution")
myRequest.ok_filenames_list.append("statistique_stmg")
myRequest.ok_filenames_list.append("comparaison")
myRequest.ok_filenames_list.append("suites_numer")
myRequest.ok_filenames_list.append("suites_arith")
myRequest.ok_filenames_list.append("eqs_droites")
myRequest.ok_filenames_list.append("derr_tangente")
myRequest.ok_filenames_list.append("suites_geom")
myRequest.ok_filenames_list.append("troisieme_deg")
myRequest.ok_filenames_list.append("derr_var")
myRequest.ok_filenames_list.append("intervalle_confiance")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")

if "--no-external" in sys.argv :
    myRequest.add_plugin(commun.set_no_useexternal,"after_pytex")
