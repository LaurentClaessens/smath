#! /usr/bin/python
# -*- coding: utf8 -*-

import latexparser
import latexparser.PytexTools
import commun
import enseignement

tous=enseignement.tous
groupe_5B=enseignement.groupe_5B
groupe_5AB=enseignement.groupe_5AB


DS2_5AB=commun.TheDS("DS2_5AB",groupe_5AB,4)
DS1_5B=commun.TheDS("DS1_5B",groupe_5B,1)
DS_5B3=commun.TheDS("DS_5B3",groupe_5B,1)
DS_5B4=commun.TheDS("DS_5B4",groupe_5B,1)
DS_5B4rattrap=commun.TheDS("DS_5B4rattrap",groupe_5B,1)
DS_5B5=commun.TheDS("DS_5B5",groupe_5B,1)
DS_5B6=commun.TheDS("DS_5B6",groupe_5B,0,n_student=1)
DS_5B7=commun.TheDS("DS_5B7",groupe_5B,0,n_student=1)
DS_5B75=commun.TheDS("DS_5B75",groupe_5B,0,n_student=1)
DS_5B8=commun.TheDS("DS_5B8",groupe_5B,0,n_student=1)
DS_5B85=commun.TheDS("DS_5B85",groupe_5B,0,n_student=1)

jeveux=DS_5B85
jeveux.write_the_file()

myRequest = latexparser.PytexTools.Request("seconde")
myRequest.original_filename=jeveux.tex_filename
myRequest.ok_filenames_list=jeveux.ok_filenames_list()
myRequest.add_plugin(jeveux.set_filename,"medicament")

#% ATTENTION : lorsqu'on compile avec lst_ds*.py, les versions plus grandes sont à vérifier.
#%    En particulier il y a parfois des choses en multicolonne qui ne passent pas bien.
