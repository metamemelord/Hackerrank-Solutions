#!/bin/python3


# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

import sys
sys.setrecursionlimit(10000)

d = {}
def getWays(n, x, index):
    if n == 0:
        return 1
    elif n<0 or index == len(x):
        return 0
    if (n,index) in d:
        return d[(n,index)]
    count = 0
    '''
    k = 0
    while k<=n:
        count += getWays(n-k,c,index+1)
        k += c[index]
    '''
    k = n
    while k>=0:
        count += getWays(k,c,index+1)
        k -= c[index]
    d[(n,index)] = count
    return count
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
print(getWays(n,c,0))
