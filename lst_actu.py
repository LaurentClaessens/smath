#! /usr/bin/python
# -*- coding: utf8 -*-

import commun
import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("4_priorite")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")

myRequest.new_output_filename="0-actu.pdf"
