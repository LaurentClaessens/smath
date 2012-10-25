# -*- coding: utf8 -*-

import datetime

class Croix(object):
    def __init__(self,jour,mois,an,motif):
        self.datetime=datetime.datetime(an,mois,jour,12,12)
        self.motif=motif

class Colle(object):
    def __init__(self,jour,mois,an,motif):
        self.datetime=datetime.datetime(an,mois,jour,12,12)
        self.motif=motif

class Student(object):
    def __init__(self,groupe=""):
        self.groupe=groupe
        self.croix=[]
        self.old_croix=[]
        self.colle=[]
        self.nom=""
        self.prenom=""
    def append_bar(self,jour,mois,an,motif):
        self.croix.append(Croix(jour,mois,an,motif))
    def append_colle(self,jour,mois,an,motif=None):
        """
        Si on ne donne pas de motifs, c'est les croix obtenues jusqu'alors.
        """
        self.old_croix.extend(self.croix)
        if motif=None:
            motif="\n".join([x.motif for x in self.croix])
        self.colle.append(Colle(jour,mois,an,motif))
        self.croix=[]

seconde_deux={}
seconde_deux[("Atzorivenne","Mathis")]=Student(groupe="2nd2")
seconde_deux[("Bailly","Thomas")]=Student(groupe="2nd2")
seconde_deux[("Bauche","Léa")]=Student(groupe="2nd2")
seconde_deux[("Besancon","Séphora")]=Student(groupe="2nd2")
seconde_deux[("Besnier","Romain")]=Student(groupe="2nd2")
seconde_deux[("Blanchot","Noé")]=Student(groupe="2nd2")
seconde_deux[("Caretti","Arno")]=Student(groupe="2nd2")
seconde_deux[("Colin","Mathieu")]=Student(groupe="2nd2")
seconde_deux[("Dole","Cynthia")]=Student(groupe="2nd2")
seconde_deux[("Dominot","Charline")]=Student(groupe="2nd2")
seconde_deux[("Giroux","Adeline")]=Student(groupe="2nd2")
seconde_deux[("Gras","Guillaume")]=Student(groupe="2nd2")
seconde_deux[("Guenard","Florian")]=Student(groupe="2nd2")
seconde_deux[("Guillot","Anthony")]=Student(groupe="2nd2")
seconde_deux[("Koehler","Paul-Erwan")]=Student(groupe="2nd2")
seconde_deux[("Kuti","Belinda")]=Student(groupe="2nd2")
seconde_deux[("Larderet","Etienne")]=Student(groupe="2nd2")
seconde_deux[("Letondor-Lavrut","Claire")]=Student(groupe="2nd2")
seconde_deux[("Limoge","Thibaut")]=Student(groupe="2nd2")
seconde_deux[("Mougeot","Romain")]=Student(groupe="2nd2")
seconde_deux[("Navel","Rémi")]=Student(groupe="2nd2")
seconde_deux[("Pardon","Mélanie")]=Student(groupe="2nd2")
seconde_deux[("Perrault","Mélanie")]=Student(groupe="2nd2")
seconde_deux[("Pillot","César")]=Student(groupe="2nd2")
seconde_deux[("Préaud","Raphaël")]=Student(groupe="2nd2")
seconde_deux[("Robert","Jérémy")]=Student(groupe="2nd2")
seconde_deux[("Tépinier","Laura")]=Student(groupe="2nd2")
seconde_deux[("Thevenot","Bastien")]=Student(groupe="2nd2")
seconde_deux[("Villet","Océane")]=Student(groupe="2nd2")
seconde_deux[("Virion","Valentin")]=Student(groupe="2nd2")

seconde_six={}
seconde_six[("Badets","Marine")]=Student(groupe="2nd6")
seconde_six[("Badot","Kévin")]=Student(groupe="2nd6")
seconde_six[("Bellaton","Pénélope")]=Student(groupe="2nd6")
seconde_six[("Bôle-Richard","Elodie")]=Student(groupe="2nd6")
seconde_six[("Bourgeois","Bryan")]=Student(groupe="2nd6")
seconde_six[("Brenot","Romain")]=Student(groupe="2nd6")
seconde_six[("Chapoutot","Marine")]=Student(groupe="2nd6")
seconde_six[("Chopard","Mickaël")]=Student(groupe="2nd6")
seconde_six[("Corand","Manon")]=Student(groupe="2nd6")
seconde_six[("Cousseau","Florine")]=Student(groupe="2nd6")
seconde_six[("Cretin","Rebecca")]=Student(groupe="2nd6")
seconde_six[("Cuevas","Gabrielle")]=Student(groupe="2nd6")
seconde_six[("Delhaye","Fiona")]=Student(groupe="2nd6")
seconde_six[("Di-Natale","Romain")]=Student(groupe="2nd6")
seconde_six[("Dormoy","Adrien")]=Student(groupe="2nd6")
seconde_six[("Dubief","Valentin")]=Student(groupe="2nd6")
seconde_six[("Dubrulle","Amandine")]=Student(groupe="2nd6")
seconde_six[("Fogel","Axel")]=Student(groupe="2nd6")
seconde_six[("Fontellini","Julie")]=Student(groupe="2nd6")
seconde_six[("Grenot","Emmanuel")]=Student(groupe="2nd6")
seconde_six[("Guyot","Coralie")]=Student(groupe="2nd6")
seconde_six[("Lebrasseur","Fabien")]=Student(groupe="2nd6")
seconde_six[("Leroux","Alexia")]=Student(groupe="2nd6")
seconde_six[("Mathieu","Clara")]=Student(groupe="2nd6")
seconde_six[("Moret","Manon")]=Student(groupe="2nd6")
seconde_six[("Moustakim","Ilhem")]=Student(groupe="2nd6")
seconde_six[("Paris","Joël")]=Student(groupe="2nd6")
seconde_six[("Pellegrini","Clara")]=Student(groupe="2nd6")
seconde_six[("Piguet","Louise")]=Student(groupe="2nd6")
seconde_six[("Quéré","Léa")]=Student(groupe="2nd6")
seconde_six[("Rodrigues","Maëva")]=Student(groupe="2nd6")
seconde_six[("Schindler","Sandra")]=Student(groupe="2nd6")

stmg={}
stmg[("Aucant","Anaïs")]=Student(groupe="1stmg1")
stmg[("Babet","Mauranne")]=Student(groupe="1stmg1")
stmg[("Benlarbi","Fayçal")]=Student(groupe="1stmg1")
stmg[("Bongain","Marie")]=Student(groupe="1stmg1")
stmg[("Bonnevie","Quentin")]=Student(groupe="1stmg1")
stmg[("Boujon","Agathe")]=Student(groupe="1stmg1")
stmg[("Chenut","Stéphane")]=Student(groupe="1stmg1")
stmg[("Chourfi","Marwa")]=Student(groupe="1stmg1")
stmg[("Da Mota-Païs","Ophélie")]=Student(groupe="1stmg1")
stmg[("Drissi","M'hamed")]=Student(groupe="1stmg1")
stmg[("Ekti","Melda")]=Student(groupe="1stmg1")
stmg[("Esquirol","Antoine")]=Student(groupe="1stmg1")
stmg[("Favre","Caroline")]=Student(groupe="1stmg1")
stmg[("Hachadi","Houda")]=Student(groupe="1stmg1")
stmg[("Hierholzer","Athénaïs")]=Student(groupe="1stmg1")
stmg[("Jacinto","Sarah")]=Student(groupe="1stmg1")
stmg[("Labourot","Manon")]=Student(groupe="1stmg1")
stmg[("Lesage","Kévin")]=Student(groupe="1stmg1")
stmg[("Matrat","Noémie")]=Student(groupe="1stmg1")
stmg[("Menetrier","Gautier")]=Student(groupe="1stmg1")
stmg[("Moustakim","Noëlla")]=Student(groupe="1stmg1")
stmg[("Petitjean","Marie-Lou")]=Student(groupe="1stmg1")
stmg[("Philippe","Élise")]=Student(groupe="1stmg1")
stmg[("Quenillet","Paul")]=Student(groupe="1stmg1")
stmg[("Raud","Lindsey")]=Student(groupe="1stmg1")
stmg[("Rizet","Lauraleen")]=Student(groupe="1stmg1")
stmg[("Rolet","Léo")]=Student(groupe="1stmg1")
stmg[("Rouffet","Pauline")]=Student(groupe="1stmg1")
stmg[("Soussigne","Ambre")]=Student(groupe="1stmg1")
stmg[("Verjus","Océane")]=Student(groupe="1stmg1")

tous={}
tous.update(seconde_deux)
tous.update(seconde_six)
tous.update(stmg)

for k in tous.keys():
    tous[k].nom=k[0]
    tous[k].prenom=k[1]

for et in tous.values():
    print(et.prenom,et.nom)


tous[("Atzorivenne","Mathis")].append_bar(1,10,9999,"DM pas fait : melons et pommes")
tous[("Atzorivenne","Mathis")].append_bar(12,10,2012,"Lance un objet")

#Bailly, Thomas
#Bauche, Léa

tous[("Besancon","Séphora")].append_bar(1,10,9999,"DM pas fait : melons et pommes")


tous[("Besnier","Romain")].append_bar(22,10,2012,"bavardage")
tous[("Besnier","Romain")].append_bar(28,9,2012,"Lancer un objet"
tous[("Besnier","Romain")].append_bar(8,10,2012,"est debout")
tous[("Besnier","Romain")].append_bar(15,10,2012,"est debout")
tous[("Besnier","Romain")].append_bar(1,1,999,"DM pas fait : melons et pommes")
tous[("Besnier","Romain")].append_bar(15,10,2012,"siffle")

tous[("Besnier","Romain")].append_colle(16,10,2012,motif=None)
print(tous[("Besnier","Romain")].colles[0].motif)



"""


========================================================
Blanchot, Noé
bavardage le 11 octobre
bavardage le 12 octobre
bavardage le 15 octobre
bavardage pendant l'interrogation le 19 octobre
bavardage 22 octobre


A déjà une colle pour motif
Bavardage incessant depuis le début du mois d'octobre, y compris pendant la séance en salle informatique.

Les croix correspondantes : 1 octobre            4 octobre            8 octobre            8 octobre pendant la séance informatique


=======================================================

Caretti, Arno
Debout : 1 octobre
DM pas fait : melons et pommes


=======================================================
Colin, Mathieu
Lance le 15 octobre
bruitage et bavardage incessant le 15 octobre
cahier fermé le 19 octobre
bavardage 22 octobre
=======================================================


=======================================================
Dole, Cynthia
Parle avec Noé tout le cours en groupe du 15 octobre

=======================================================

Dominot, Charline
Giroux, Adeline

=======================================================
Gras, Guillaume
Bavardage le 1 octobre
debout le 1 octobre
bavardage le 15 octobre
bavardage 22 octobre

=======================================================

Guenard, Florian

=======================================================
Guillot, Anthony
debout le 1 octobre
bavardage le 11 octobre
cahier fermé le 12 octobre
=======================================================



=======================================================
Koehler, Paul-Erwan
DM pas fait : histogramme
            melons et pommes
bavardage le 11 octobre
se chamaille en continu avec Raphaël le 12 octobre

=======================================================


=======================================================
Kuti, Belinda
DM pas fait : histogrammes
cahier fermé le 12 octobre
prend le sac de Bastien lorsque ce dernier a le dos tourné.
Parle trop et fait la chèvre le 22 octobre

=======================================================

Larderet, Etienne

=======================================================
Letondor-Lavrut, Claire
Lancer un objet : 4 octobre
prend le sac de Bastien lorsque ce dernier a le dos tourné.
parle trop le 22 octobre

=======================================================

Limoge, Thibaut
bavardage le 11 octobre
bavardage 22 octobre

=======================================================
Mougeot, Romain

=======================================================
Navel, Rémi
Bavardage le 4 octobre
crée des répertoires aux noms idiots en salle info le 8 octobre
bavardage le 11 octobre
bavardage le 12 octobre

=======================================================

=======================================================
Pardon, Mélanie
DM pas fait : melons et pommes
bavardage le 11 octobre

=======================================================

Perrault, Mélanie

=======================================================
Pillot, César
Bavardage : 1 octobre
DM pas fait : histogramme
=======================================================


=======================================================
Préaud, Raphaël
Bavardage le 1 octobre
frappe César avec un stylo le 4 octobre
se chamaille en continu avec Paul-Erwan le 12 octobre
bavardage 22 octobre (tant en groupe qu'en classe complète)

=======================================================

=======================================================
Robert, Jérémy
bavardage 22 octobre



Prend une seconde retenue (rédigée le 22 octobre)
Jette sa trousse par la fenêtre et sort de la classe de son propre chef pour aller la chercher, malgré une interdiction totalement explicite du professeur.
Son excuse : «j'ai pas fait exprès : je visais Rémi».


Prend une retenue (rédigée le 16 octobre). Motif :
Bavardage le 1 octobre
insulte Raphaël à haute voix le 12 octobre et le 15 octobre
cahier fermé le 12 octobre
tente de coller du papier collant sur Laura le 15 octobre
cahier fermé le 15 octobre


=======================================================

=======================================================
Tepinier, Laura
Bavardage le 4 octobre
bavardage le 11 octobre
cahier fermé le 12 octobre
bavardage 22 octobre
cahier ouvert avant la fin du cours le 22 octobre
=======================================================

Thevenot, Bastien
bavardage 22 octobre

=======================================================
Villet, Océane
cahier fermé le 12 octobre
cahier fermé le 15 octobre
lance une bouteille d'eau le 19 octobre
=======================================================
Virion, Valentin
bavardage le 11 octobre

=======================================================
Paul 
Debout le 28 sept
debout (re) le 28 sept
=======================================================


Badets, Marine
Badot, Kévin
Bellaton, Pénélope

============================================
Bôle-Richard, Elodie
Bavardage le 8 octobre
bavardage le 16 octobre
============================================

============================================
Bourgeois, Bryan
bavardage le 22 octobre
============================================



Brenot, Romain
Chapoutot, Marine

============================================
Chopard, Mickaël
bavardage en continu avec Gabrielle et Rebecca le 16 octobre
pré-colle le 16 octobre
bavardage le 22 octobre (toujours avec Gabrielle et Rebecca)
============================================

Corand, Manon
Cousseau, Florine
============================================
Cretin, Rebecca
bavardage en continu avec Mickaël et Gabrielle le 16 octobre
pré-colle le 16 octobre
bavardage le 22 octobre
============================================

============================================
Cuevas, Gabrielle
bavardage en continu avec Mickaël et Rebecca le 16 octobre
bavardage le 22 octobre (idem en continu avec Mickaël et Rebecca)
============================================
Delhaye, Fiona

============================================
Di-Natale, Romain
pré-colle le 16 octobre
bavardage le 22 octobre
============================================

============================================
Dormoy, Adrien
cahier fermé + bavardage le 16 octobre
pré-colle le 16 octobre
bavardage le 22 octobre
============================================

Dubief, Valentin
Dubrulle, Amandine
Fogel, Axel
Fontellini, Julie
Grenot, Emmanuel

============================================
Guyot, Coralie
Durant la séance informatique du 11 octobre, cherche des images d'Apu sur internet
=============================================


Lebrasseur, Fabien
Leroux, Alexia
Mathieu, Clara
Moret, Manon

=============================================
Moustakim, Ilhem
bavardage le 8 octobre
Durant la séance informatique du 11 octobre, cherche des images d'Apu sur internet
chante en cœur avec Louise + bavardage le 16 octobre
bavardage le 22 octobre
=============================================


Paris, Joël

=============================================
Pellegrini, Clara
bavardage le 16 octobre
bavardage le 22 octobre
=============================================
Piguet, Louise
chante en cœur avec Ilhem le 16 octobre
=============================================

=============================================
Quéré, Léa
bavardage le 16 octobre
pré-colle le 16 octobre (répète «le premier qui moufte ...» pour se moquer du prof)
=============================================
Rodrigues, Maëva
bavardage le 16 octobre
=============================================



Schindler, Sandra





Les pré-colles
Athénaïs
Jacinto, Sarah
Ambre



Aucant, Anaïs
Bavardage 15 octobre


Babet, Mauranne
bavardage 15 octobre


Benlarbi, Fayçal


==================================================
Bongain, Marie
Bavardage le 15 octobre

==================================================
Bonnevie, Quentin
Bavarde (8 octobre)
==================================================

Boujon, Agathe
Bavardage 15 octobre
bavardage le 19 octobre
==================================================


Chenut, Stéphane

==================================================
Chourfi, Marwa
Cahier fermé le 2 octobre
bavardage le 19 octobre
==================================================

Da Mota-Païs, Ophélie

==================================================
Drissi, M'hamed
joue avec un briquet en classe (8 octobre)
bavarde (8 octobre)
bavardage le 16 octobre
==================================================


Ekti, Melda

==================================================
Esquirol, Antoine
bavardage 15 octobre
bavardage le 16 octobre


A eu une colle
Motif :
A un téléphone en main durant le cours du 8 octobre. 
Note a posteriori : n'assume pas ses responsabilités : a laissé Agathe se dénoncer à sa place.

==================================================


Favre, Caroline
Hachadi, Houda

==================================================
Hierholzer, Athénaïs
Lancer : 1 octobre
Bavarde (8 octobre)
bavardage (15 octobre)
pré-colle (19 octobre)
==================================================
Jacinto, Sarah
Labourot, Manon
pré-colle le 16 octobre

==================================================
Lesage, Kévin
Bavarde trop (8 octobre)
15 octobre

A déjà pris une retenue pour motif :
Le 2 octobre 2012
Colle cumulative. Est debout (2 oct), a un cahier fermé alors que le cours n'est pas fini (1 oct) et bavardage.
Cette colle a été faite le 17 octobre et les exercices ont été fait de façon complètement fausses.

===================================================



Matrat, Noémie
bavardage le 16 octobre
==================================================
Menetrier, Gautier
debout le 2 octobre 
debout (re) le 2 octobre 
==================================================


==================================================
Moustakim, Noëlla
Bavardage le 19 octobre
==================================================

Petitjean, Marie-Lou
Philippe, Élise
Quenillet, Paul
Raud, Lindsey
15 octobre


==============================================
Rizet, Lauraleen
bavardage le 16 octobre

A déjà une colle pour motif :
A un téléphone en main durant le cours du 2 octobre. Préfère avoir une colle que de voir le téléphone confisqué chez le CPE.

==============================================
Rolet, Léo
Rouffet, Pauline

==============================================
Soussigne, Ambre
bavardage le 2 octobre
debout le 2 octobre
cahier fermé le 12 octobre
pré-colle le 16 octobre
==============================================


Verjus, Océane



"""
