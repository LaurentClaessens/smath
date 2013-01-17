#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("feuilles")
myRequest.original_filename="exos_interros.tex"

myRequest.ok_filenames_list=["e_smath"]
