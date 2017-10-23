# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 01:15:56 2017

@author: MetaMemeLord-
"""

x = [int(input()) for _ in range(int(input()))]
a = [0]*len(x)
for i in range(1,len(x)):
    if x[i-1] < x[i]:
        a[i] = a[i-1] + 1
for i in range(len(x)-2,-1,-1):
    if x[i+1] < x[i]:
        val = a[i+1] + 1
    else:
        val = 0
    a[i] = max(val,a[i])
#print(a)
print(len(x)+sum(a))