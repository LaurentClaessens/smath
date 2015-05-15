#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun
import enseignement

tous=enseignement.tous
groupe_5A=enseignement.groupe_5A
groupe_5AB=enseignement.groupe_5AB


DS2_5AB=commun.TheDS("DS2_5AB",groupe_5AB,4)
DS_5A3=commun.TheDS("DS_5A3",groupe_5A,0,n_student=1)
DS_5A4=commun.TheDS("DS_5A4",groupe_5A,0,n_student=1)
DS_5A5=commun.TheDS("DS_5A5",groupe_5A,1,n_student=1)
DS_5A6=commun.TheDS("DS_5A6",groupe_5A,0,n_student=1)
DS_5A7=commun.TheDS("DS_5A7",groupe_5A,0,n_student=1)

jeveux=DS_5A6
jeveux.write_the_file()

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename=jeveux.tex_filename
myRequest.ok_filenames_list=jeveux.ok_filenames_list()
myRequest.add_plugin(jeveux.set_filename,"medicament")
