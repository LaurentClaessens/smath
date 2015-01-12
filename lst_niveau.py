#! /usr/bin/python
# -*- coding: utf8 -*-

import sys
import commun
import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

#myRequest.ok_filenames_list=["e_smath"]

if "cinquième" in sys.argv:
    ok_mark_list=commun.cinquieme_mark_list
if "quatrième" in sys.argv:
    ok_mark_list=commun.quatrieme_mark_list
if "seconde" in sys.argv:
    ok_mark_list=commun.seconde_mark_list
if "première" in sys.argv:
    ok_mark_list=commun.premiere_mark_list
if "autre" in sys.argv:
    ok_mark_list=commun.autre_mark_list

myRequest.add_plugin(LaTeXparser.PytexTools.accept_all_input,"medicament")
myRequest.add_plugin(LaTeXparser.PytexTools.keep_script_marks(ok_mark_list),"before_pytex")
if "--no-external" in sys.argv :
    myRequest.add_plugin(commun.set_no_useexternal,"after_pytex")

