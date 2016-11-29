#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import latexparser
import latexparser.PytexTools

myRequest = latexparser.PytexTools.Request("seconde")
#myRequest.original_filename="smath.tex"

def accept_all_input(medicament):
    medicament.accept_input=lambda x: True

myRequest.add_plugin(accept_all_input,"medicament")

myRequest.original_filename="secours_cinquieme.tex"
