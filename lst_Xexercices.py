#! /usr/bin/python
# -*- coding: utf8 -*-

import latexparser
import latexparser.PytexTools

myRequest = latexparser.PytexTools.Request("seconde")
myRequest.original_filename="Xexercices.tex"

myRequest.ok_filenames_list=["e_smath"]
