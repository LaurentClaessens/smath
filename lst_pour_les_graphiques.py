#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="pour_les_graphiques.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("seconde")
