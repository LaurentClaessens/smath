#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="automatedChapter.tex"


def set_filename(medicament):
    medicament.new_output_filename="0-actu5A.pdf"

fract=commun.OneChapter("Écriture fractionnaire","5Aexercices.tex")
droites_rem=commun.OneChapter("Droites remarquables dans un triangle","5Aexercices.tex")
ops_frac=commun.OneChapter("Opérations sur les fractions","5Aexercices.tex")
exp_litt=commun.OneChapter("Expressions littérales","5Aexercices.tex")

# À la rentrée de novembre, je continue les opérations sur les fractions.
# Donc ici je prépare les expressions littérales

actu5=exp_litt
actu5.set_filename=set_filename
actu5.write_the_file()

myRequest.add_plugin(actu5.set_filename,"medicament")
myRequest.ok_filenames_list=actu5.ok_filenames_list()
