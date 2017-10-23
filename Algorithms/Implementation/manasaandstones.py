# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:45:40 2017

@author: MetaMemeLord-
"""
for _ in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())
    if b<a:
        a,b = b,a
    if a==b:
        print(a*(n-1))
    else:
        print(' '.join(map(str,sorted({a*x+b*(n-x-1) for x in range(n)}))))
