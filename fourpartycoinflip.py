#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:27:33 2018

@author: bram
"""

import time

from protocol import Coinflip


def main():
    arr = ["Alice", "Bob", "Charlie", "David"]
    leaderChooser = Coinflip(arr)
    return leaderChooser.leader()

d = dict()
d['Alice'] = 0
d['Bob'] = 0
d['Charlie'] = 0
d['David'] = 0
for i in range(0,20):
        print(i)
        d[main()] += 1
print(d)

