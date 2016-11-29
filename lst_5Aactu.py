#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import latexparser
import latexparser.PytexTools
import commun

myRequest = latexparser.PytexTools.Request("seconde")
myRequest.original_filename="automatedChapter.tex"

def set_filename(medicament):
    medicament.new_output_filename="0-actu5A.pdf"

classe="5A"
fract=commun.OneChapter("Écriture fractionnaire",classe)
droites_rem=commun.OneChapter("Droites remarquables dans un triangle",classe)
ops_frac=commun.OneChapter("Opérations sur les fractions",classe)
exp_litt=commun.OneChapter("Expressions littérales",classe)
sym_centrale=commun.OneChapter("Symétrie centrale",classe)
nombres_relatifs=commun.OneChapter("Nombres relatifs",classe)
ang_parall=commun.OneChapter("Angles et parallélisme",classe)
proportionnali=commun.OneChapter("Proportionnalité",classe)
ops_rel=commun.OneChapter("Nombres relatifs : opérations",classe)
afp=commun.OneChapter("Aires de figures planes",classe)

actu5=afp
actu5.set_filename=set_filename
actu5.write_the_file()

myRequest.add_plugin(actu5.set_filename,"medicament")
myRequest.ok_filenames_list=actu5.ok_filenames_list()
