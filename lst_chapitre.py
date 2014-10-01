#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

chapter_title="Opérations sur les écritures fractionnaires"

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="automatedChapter.tex"


def smath_input_line():
    smath_lines=open("smath.tex").readlines()
    for i,l in enumerate(smath_lines):
        if chapter_title in l:
            line=i
    return smath_lines[line+1]

def exercice_lines(filename):
    el=open(filename).readlines()
    for i,l in enumerate(el):
        if chapter_title in l:
            i_line=i+1
    f_line=i_line+1
    while "\section" not in el[f_line] and "\end{document}" not in el[f_line] :
        f_line=f_line+1
    f_line=f_line-1
    sublist=el[i_line:f_line]
    return "".join(sublist)
    

iline=smath_input_line()
exos=exercice_lines("5Bexercices.tex")

generic_lines="".join(open("genericChapter.tex").readlines())
text=generic_lines.replace("TITRE_CHAPITRE",chapter_title).replace("LES_INPUT",iline).replace("LISTE_EXERCICES",exos)

f=open("automatedChapter.tex",'w')
f.write(text)
f.close()

input_filename=iline.replace("\chapter{","").replace("}","")

myRequest.ok_filenames_list=["e_smath"]
myRequest.ok_filenames_list.append(input_filename)
myRequest.ok_filenames_list.append("<++>")
