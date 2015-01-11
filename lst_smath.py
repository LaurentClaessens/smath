#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import sys
import LaTeXparser
import LaTeXparser.PytexTools
import commun

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

def set_corrPosition_and_Draft(A):
    u="\corrPosition{1}"
    v="\corrPosition{2}"
    A = A.replace(u, v)
    u="\corrPosition{2}"
    A = A.replace(u, v)
    u="\corrDraft"
    A=A.replace(u,"%")
    return A

def accept_all_input(medicament):
    medicament.accept_input=lambda x: True

myRequest.add_plugin(accept_all_input,"medicament")
myRequest.add_plugin(set_corrPosition_and_Draft,"after_pytex")


if "--no-external" in sys.argv :
    myRequest.add_plugin(commun.set_no_useexternal,"after_pytex")

myRequest.original_filename="smath.tex"
