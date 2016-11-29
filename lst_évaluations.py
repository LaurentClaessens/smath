#! /usr/bin/python
# -*- coding: utf8 -*-

import commun
import latexparser
import latexparser.PytexTools

myRequest = latexparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("15_evaluation5")
myRequest.ok_filenames_list.append("16_evaluation4")
myRequest.ok_filenames_list.append("50_devoirs5")
myRequest.ok_filenames_list.append("49_devoirs4")
myRequest.ok_filenames_list.append("<++>")

myRequest.add_plugin(commun.set_filename("0-évaluations.pdf"),"medicament")
