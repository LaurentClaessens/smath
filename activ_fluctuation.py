#! /usr/bin/python3
# -*- coding: utf8 -*-

import random

def experience():
    n_succes=0
    for i in range(0,100):
        x=random.uniform(0,1)
        if x < 0.3 :
            n_succes = n_succes +1
    return n_succes


def multi_xp(n):
    for k in range(0,n):
        print(experience())


multi_xp(15)
