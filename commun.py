class OneChapter(object):
    def __init__(self,chapter_title,exercice_filename):
        self.chapter_title=chapter_title
        self.exercice_filename=exercice_filename
        self.input_filename=self.smath_input_line().replace("\input{","").replace("}","").replace("\n","")
    def smath_input_line(self):
        smath_lines=open("smath.tex").readlines()
        for i,l in enumerate(smath_lines):
            if self.chapter_title in l:
                line=i
        return smath_lines[line+1]
    def count_exo(self,text,i_line):
        """
        return the number of \Exo in 'text' from the beginning and the line number 'i_line'.
        """
        lines=text.split("\n")[0:i_line]
        n=0
        for l in lines:
            ll=l.replace(" ","")
            if ll.startswith("\Exo"):
                n=n+1
        return n
    def exercice_lines(self,filename):
        el=open(filename).readlines()
        for i,l in enumerate(el):
            if self.chapter_title in l:
                i_line=i+1
        f_line=i_line+1
        while "\section" not in el[f_line] and "\end{document}" not in el[f_line] :
            f_line=f_line+1
        f_line=f_line-1
        exo=self.count_exo("".join(el),i_line)
        sublist=["\setcounter{{CountExercice}}{{{}}}".format(exo)]
        sublist.extend(el[i_line:f_line])
        return "".join(sublist)
    def write_the_file(self,filename="automatedChapter.tex"):
        generic_lines="".join(open("genericChapter.tex").readlines())
        text=generic_lines.replace("TITRE_CHAPITRE",self.chapter_title).replace("LES_INPUT",self.smath_input_line()).replace("LISTE_EXERCICES",self.exercice_lines(self.exercice_filename))
        f=open(filename,'w')
        f.write(text)
        f.close()
    def set_filename(self,medicament):
        medicament.new_output_filename="0-chapitre_"+self.chapter_title.replace(' ',"_")+".pdf"
    def ok_filenames_list(self):
        a=["e_smath"]
        a.append(self.input_filename)
        return a
