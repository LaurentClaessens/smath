#! /usr/bin/sage -python
# -*- coding: utf8 -*-

import cProfile
from phystricks import *

from phystricksLVNXooEXEvoV import LVNXooEXEvoV
from phystricksJJHQooEkspEV import JJHQooEkspEV

def profile_me():
    cProfile.run("JJHQooEkspEV()")
    return "ok"

profile_me()
