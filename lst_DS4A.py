#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun
import enseignement

tous=enseignement.tous
groupe_4A=enseignement.groupe_4A


DS2_4A=commun.TheDS("DS2_4A",groupe_4A,1)
DS_4A3=commun.TheDS("DS_4A3",groupe_4A,1)
DS_4A4=commun.TheDS("DS_4A4",groupe_4A,0)
DS_4A5=commun.TheDS("DS_4A5",groupe_4A,0)
DS_4A6=commun.TheDS("DS_4A6",groupe_4A,0,n_student=1)

jeveux=DS_4A6
jeveux.write_the_file()

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename=jeveux.tex_filename
myRequest.ok_filenames_list=jeveux.ok_filenames_list()
myRequest.add_plugin(jeveux.set_filename,"medicament")
