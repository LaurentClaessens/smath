#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("3_relatifs4")
myRequest.ok_filenames_list.append("6_exercices_feuilles_quatrieme")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
