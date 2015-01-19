# -*- coding: utf8 -*-

#from __future__ import unicode_literals

cinquieme_mark_list=[]
cinquieme_mark_list.append("% SCRIPT MARK -- PREAMBLE")
cinquieme_mark_list.append("% SCRIPT MARK -- BEGIN DOCUMENT")
cinquieme_mark_list.append("% SCRIPT MARK -- TABLE DES MATIÈRES")
cinquieme_mark_list.append("% SCRIPT MARK -- CINQUIÈME")
cinquieme_mark_list.append("% SCRIPT MARK -- CORRECTIONS")
cinquieme_mark_list.append("% SCRIPT MARK -- FINAL")

quatrieme_mark_list=[]
quatrieme_mark_list.append("% SCRIPT MARK -- PREAMBLE")
quatrieme_mark_list.append("% SCRIPT MARK -- BEGIN DOCUMENT")
quatrieme_mark_list.append("% SCRIPT MARK -- TABLE DES MATIÈRES")
quatrieme_mark_list.append("% SCRIPT MARK -- QUATRIÈME")
quatrieme_mark_list.append("% SCRIPT MARK -- CORRECTIONS")
quatrieme_mark_list.append("% SCRIPT MARK -- FINAL")

seconde_mark_list=[]
seconde_mark_list.append("% SCRIPT MARK -- PREAMBLE")
seconde_mark_list.append("% SCRIPT MARK -- BEGIN DOCUMENT")
seconde_mark_list.append("% SCRIPT MARK -- TABLE DES MATIÈRES")
seconde_mark_list.append("% SCRIPT MARK -- SECONDE")
seconde_mark_list.append("% SCRIPT MARK -- CORRECTIONS")
seconde_mark_list.append("% SCRIPT MARK -- FINAL")

premiere_mark_list=[]
premiere_mark_list.append("% SCRIPT MARK -- PREAMBLE")
premiere_mark_list.append("% SCRIPT MARK -- BEGIN DOCUMENT")
premiere_mark_list.append("% SCRIPT MARK -- TABLE DES MATIÈRES")
premiere_mark_list.append("% SCRIPT MARK -- PREMIÈRE")
premiere_mark_list.append("% SCRIPT MARK -- CORRECTIONS")
premiere_mark_list.append("% SCRIPT MARK -- FINAL")

autre_mark_list=[]
autre_mark_list.append("% SCRIPT MARK -- PREAMBLE")
autre_mark_list.append("% SCRIPT MARK -- BEGIN DOCUMENT")
autre_mark_list.append("% SCRIPT MARK -- TABLE DES MATIÈRES")
autre_mark_list.append("% SCRIPT MARK -- AUTRE")
autre_mark_list.append("% SCRIPT MARK -- CORRECTIONS")
autre_mark_list.append("% SCRIPT MARK -- FINAL")


class OneChapter(object):
    def __init__(self,chapter_title,group):
        self.group=group
        self.chapter_title=chapter_title
        self.exercice_filename=self.group+"exercices.tex"
        self.input_filename=self.smath_input_line().replace("\input{","").replace("}","").replace("\n","")
        self._count_section=0
    def smath_input_line(self):
        smath_lines=open("smath.tex").readlines()
        for i,l in enumerate(smath_lines):
            if self.chapter_title in l:
                line=i
        return smath_lines[line+1]
    def preamble_lines(self):
        import LaTeXparser
        import LaTeXparser.PytexTools
        A=LaTeXparser.FileToCodeLaTeX("smath.tex",keep_comments=True)
        script_mark_dict=LaTeXparser.PytexTools.script_mark_dict(A)
        a,b=script_mark_dict["% SCRIPT MARK -- PREAMBLE"]
        text="\n".join(A.splitlines()[a:b])
        return text
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
    def count_section(self,text=None,i_line=None):
        """
        return the number of section from the beggining to the line number 'i_line':
        """
        if text==None:
            return self._count_section
        lines=text.split("\n")[0:i_line]
        n=0
        for l in lines:
            ll=l.replace(" ","")
            if ll.startswith("\section"):
                n=n+1
        self._count_section=n
        return n
    def exercice_lines(self,filename):
        el=open(filename).readlines()
        for i,l in enumerate(el):
            if self.chapter_title in l:
                section_line=l
                i_line=i+1
        f_line=i_line+1
        while "\section" not in el[f_line] and "\end{document}" not in el[f_line] :
            f_line=f_line+1
        f_line=f_line-1
        exo=self.count_exo("".join(el),i_line)
        section=self.count_section("".join(el),i_line)
        sublist=["\setcounter{{CountExercice}}{{{}}}".format(exo)]
        sublist.append(  "\setcounter{{section}}{{{}}}".format(section-1) )  # -1 because the \section command will add one.
        sublist.append(section_line)
        sublist.extend(el[i_line:f_line])
        return "".join(sublist)
    def write_the_file(self,filename="automatedChapter.tex"):
        generic_lines="".join(open("genericChapter.tex").readlines())
        preamble_lines=self.preamble_lines()
        text=generic_lines.replace("TITRE_CHAPITRE",self.chapter_title+" ({})".format(self.group)).replace("LES_INPUT",self.smath_input_line()).replace("LISTE_EXERCICES",self.exercice_lines(self.exercice_filename)).replace("N_CHAPITRE",str(self.count_section()-1)).replace("PREAMBLE",preamble_lines)
        f=open(filename,'w')
        f.write(text)
        f.close()
    def set_filename(self,medicament):
        medicament.new_output_filename="0-chapitre_"+self.chapter_title.replace(' ',"_")+".pdf"
    def ok_filenames_list(self):
        a=["e_smath"]
        a.append(self.input_filename)
        return a

class OnePart(object):
    """
    We consider the whole declarative part up to the first "\part" (exclusively).
    """
    def __init__(self,part_name,filename):
        self.part_name=part_name
        self.filename=filename
        self.file_text=open(self.filename).read()
    def up_to_part():
        pass

class TheDS(object):
    def __init__(self,DS_id,group,nPAI,n_student=None):
        """
        'nPAI' is the number of copies that have to be printed in larger size.
        """
        self.DS_id=DS_id
        self.group=group
        self.filename="DSs.tex"
        self.nPAI=nPAI
        self._latex_portion=None
        self.tex_filename=self.DS_id+"_long.tex"
        self.n_student=n_student
    def latex_portion(self):
        if not self._latex_portion :
            el=open(self.filename).readlines()
            for i,l in enumerate(el):
                if self.DS_id in l:
                    i_line=i+1
            f_line=i_line+1
            while "\end{feuilleDS}" not in el[f_line] :
                f_line=f_line+1
            f_line=f_line+1
            self._latex_portion="".join(el[i_line:f_line])
        return self._latex_portion
    def latex_total(self):
        code=""
        n=len(self.group.student_list)+2    # J'en ai alors 2 en trop.
        if self.n_student :
            n=self.n_student
        for i in range(0,n) :
            code=code+"\n\\newpage\n"+self.latex_portion()+"\n"
        code=code+"\n\\LARGE\n"
        for i in range(0,self.nPAI):
            code=code+"\n\\newpage\n"+self.latex_portion()+"\n"
        return code
    def write_the_file(self):
        generic_lines="".join(open("genericDS.tex").readlines())
        text=generic_lines.replace("LES_FEUILLES",self.latex_total())
        f=open(self.tex_filename,'w')
        f.write(text)
        f.close()
    def set_filename(self,medicament):
        medicament.new_output_filename="0-"+self.DS_id+".pdf"
    def ok_filenames_list(self):
        a=["e_smath"]
        a.append("automatedDS")
        return a

class Situation(object):
    """
    This serves to generate a graph and a value array in the same time.
    """
    def __init__(self,name,p1,p2,pts):
        import LaTeXparser.PytexTools
        self.name=name
        self.pts=pts
        self.p1=p1
        self.p2=p2
        dic={}
        dic[(0,0)]="\\text{"+p1+"}"
        dic[(0,1)]="\\text{"+p2+"}"
        for i,p in enumerate(pts):
            dic[(i+1,0)]=str(p[0])
            dic[(i+1,1)]=str(p[1])
        self.array=LaTeXparser.PytexTools.Array(dic)
    def write_the_file(self):
        filename=self.name+".latex"
        f=open(filename,'w')
        f.write(self.latex())
        f.close()
        print("Tableau dans le fichier",filename)
    def points_list(self):
        from phystricks import Point
        return [  Point(k[0],k[1]) for k in self.pts ]
    def latex(self):
        return self.array.latex()

class set_filename(object):
    def __init__(self,new_filename):
        self.new_filename=new_filename
    def __call__(self,medicament):
        medicament.new_output_filename=self.new_filename
