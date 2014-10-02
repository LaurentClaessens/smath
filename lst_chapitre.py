#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="automatedChapter.tex"


class OneChapter(object):
    def __init__(self,chapter_title,exercice_filename):
        self.chapter_title=chapter_title
        self.exercice_filename=exercice_filename
        self.input_filename=self.smath_input_line.replace("\input{","").replace("}","")
    def smath_input_line(self):
        smath_lines=open("smath.tex").readlines()
        for i,l in enumerate(smath_lines):
            if chapter_title in l:
                line=i
        return smath_lines[line+1]
    def exercice_lines(self,filename):
        el=open(filename).readlines()
        for i,l in enumerate(el):
            if self.chapter_title in l:
                i_line=i+1
        f_line=i_line+1
        while "\section" not in el[f_line] and "\end{document}" not in el[f_line] :
            f_line=f_line+1
        f_line=f_line-1
        sublist=el[i_line:f_line]
        return "".join(sublist)
    def write_the_file(self,filename="automatedChapter.tex"):
        generic_lines="".join(open("genericChapter.tex").readlines())
        text=generic_lines.replace("TITRE_CHAPITRE",chapter_title).replace("LES_INPUT",self.smath_input_line()).replace("LISTE_EXERCICES",exos)
        f=open(filename,'w')
        f.write(text)
        f.close()
    def ok_filenames_list(self):
        a=["e_smath"]
        a.append(self.input_filename)
        return a

    
fract=OneChapter("Opérations sur les écritures fractionnaires","5Bexercices.tex")
pythagore=OneChapter("Égalité de Pythagore","4Aexercices.tex")

pythagore.write_the_file()

myRequest.ok_filenames_list=pythagore.ok_filenames_list()
