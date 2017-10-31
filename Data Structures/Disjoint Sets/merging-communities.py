# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:55:10 2017

@author: MetaMemeLord-
"""

import sys

sys.setrecursionlimit(1000010)

def find(n):
    if x[n] == n:
        return n
    else:
        x[n] = find(x[n])
        return x[n]

def union(n1,n2):
    if n1==n2:
        return
    if n1>n2:
        n1,n2 = n2,n1
    x[n2] = n1
    s[n1] += s[n2]

n,q = map(int,input().split())
x = [i for i in range(n)]
s = [1]*n
for _ in range(q):
    m = input().split()
    if m[0] == 'M':
        union(find(int(m[1])-1),find(int(m[2])-1))
    else:
        print(s[find(int(m[1])-1)])
