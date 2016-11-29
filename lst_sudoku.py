#! /usr/bin/python
# -*- coding: utf8 -*-

import latexparser
import latexparser.PytexTools

myRequest = latexparser.PytexTools.Request("seconde")
myRequest.original_filename="sudoku.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("sudoku1")
myRequest.ok_filenames_list.append("sudoku2")
