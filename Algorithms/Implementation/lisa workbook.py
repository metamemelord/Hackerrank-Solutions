# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:59:17 2017

@author: MetaMemeLord-
"""

n,k = map(int,input().split())
pages = 1
count = 0
for i in input().split():
    i = int(i)
    j = 0
    val = 0
    while j<i:
        j += 1
        if pages == j:
            count += 1
        if j%k == 0 and j != i:
            pages += 1
    pages += 1
print(count)
