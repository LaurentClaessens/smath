#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="automatedChapter.tex"


def set_filename(medicament):
    medicament.new_output_filename="0-actu4A.pdf"

pythagore=commun.OneChapter("Égalité de Pythagore","4A")
propo=commun.OneChapter("Grandeurs proportionnelles","4A")
trig_para=commun.OneChapter("Droite des milieux","4A")
add_fract=commun.OneChapter("Addition et soustractions en écriture fractionnaire","4A")


actu4=add_fract
actu4.set_filename=set_filename
actu4.write_the_file()

myRequest.add_plugin(actu4.set_filename,"medicament")
myRequest.ok_filenames_list=actu4.ok_filenames_list()
