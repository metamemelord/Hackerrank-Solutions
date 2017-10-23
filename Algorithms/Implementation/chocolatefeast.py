# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

t = int(input().strip())
for a0 in range(t):
    n,c,m = map(int,input().strip().split(' '))
    val = n//c
    k = val
    while k != 0:
        val += k//m
        k = k%m + k//m
        if k<m:
            break
    print(val)
