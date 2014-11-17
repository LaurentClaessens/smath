#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="automatedChapter.tex"


def set_filename(medicament):
    medicament.new_output_filename="0-actu5B.pdf"

fract=commun.OneChapter("Écriture fractionnaire","5B")
droites_rem=commun.OneChapter("Droites remarquables dans un triangle","5B")
ops_frac=commun.OneChapter("Opérations sur les fractions","5B")


actu5=ops_frac
actu5.set_filename=set_filename
actu5.write_the_file()

myRequest.add_plugin(actu5.set_filename,"medicament")
myRequest.ok_filenames_list=actu5.ok_filenames_list()
