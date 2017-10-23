# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
n,k = map(int,input().split())
x = [int(i) for i in input().split()]
p = set(x)
count = 0
for i in p:
    if i+k in p:
        if i+2*k in p:
            count+=1
print(count)
