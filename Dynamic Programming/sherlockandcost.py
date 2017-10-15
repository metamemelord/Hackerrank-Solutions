# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
def dp(x):
    l,h = 0,0
    for i in range(1,len(x)):
         l, h = (max(l, h+x[i-1]-1),max(l+x[i]-1, h+abs(x[i]-x[i-1])))
    return max(l,h)
for _ in range(int(input())):
    n = int(input())
    x = [int(i) for i in input().split()]
    print(dp(x))
