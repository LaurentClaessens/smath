#! /usr/bin/python
# -*- coding: utf8 -*-

###########################################################################
#	This is the program liste_exo.py
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################

# copyright (c) Laurent Claessens, 2012
# email: moky.math@gmail.com

import os, sys

first=15
last=99

for i in range(first,last):
    f=open("ex_algo{}.py".format(i),"w")
    f.write("x")
    f.close

a=""
for i in range(first,last):
    a=a+"ex_algo{}.py ".format(i)
print(a)

for i in range(first,last):
    print("""\lstinputlisting{{ex_algo{}.py}}""".format(i))
