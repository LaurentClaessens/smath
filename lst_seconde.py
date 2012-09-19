#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("seconde")
myRequest.ok_filenames_list.append("repere")
myRequest.ok_filenames_list.append("fonctions")
myRequest.ok_filenames_list.append("stat_Pauline")
myRequest.ok_filenames_list.append("exercices_stats_descriptives")

