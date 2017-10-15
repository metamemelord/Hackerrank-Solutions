# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:12:50 2017

@author: MetaMemeLord-
"""

n,k = map(int,input().split())
x = [int(x) for x in input().split()]
for i in range(k):
    w,y = map(int,input().split())
    print(min(x[w:y+1]))
