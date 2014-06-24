#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append("0110_smath")
myRequest.ok_filenames_list.append("introSmath")
myRequest.ok_filenames_list.append("gardeSmath")
myRequest.ok_filenames_list.append("0160_autres_exercices_seconde")
myRequest.ok_filenames_list.append("autres_exercices")
myRequest.ok_filenames_list.append("autres")
myRequest.ok_filenames_list.append("APpython")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
