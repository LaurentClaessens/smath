#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="5Bexercices.tex"

myRequest.ok_filenames_list=["e_smath"]