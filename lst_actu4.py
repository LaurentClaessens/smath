#! /usr/bin/python
# -*- coding: utf8 -*-

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
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
