# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:54:29 2017

@author: MetaMemeLord-
"""

s = []
m = []
for i in range(int(input())):
    x = [int(i) for i in input().split()]
    if x[0] == 1:
        s.append(x[1])
        if len(m) == 0:
            m.append(x[1])
        elif m[-1] < x[1]:
            m.append(x[1])
        else:
            m.append(m[-1])
    elif x[0] == 2:
        m.pop()
        s.pop()
    else:
        print(m[-1])
