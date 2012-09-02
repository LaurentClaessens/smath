#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("MesEssais")
myRequest.original_filename="to_be_checked.tex"

myRequest.ok_filenames_list=[]
#myRequest.ok_filenames_list.append("<++>")
