#! /usr/bin/python
# -*- coding: utf8 -*-

import latexparser
import latexparser.PytexTools
import commun

myRequest = latexparser.PytexTools.Request("seconde")
myRequest.original_filename="5Bexercices.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.add_plugin(commun.set_filename("0-exercices5B.pdf"),"medicament")
