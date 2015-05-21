#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="Amental.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("2_mental5")
myRequest.ok_filenames_list.append("9_mental4")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.add_plugin(commun.set_filename("0-mental.pdf"),"medicament")
