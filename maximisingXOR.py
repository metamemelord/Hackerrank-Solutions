# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
x = int(input())
y = int(input())
p = str(bin(x^y))
for i in range(len(p)):
    if p[i]=='1':
        break
l = len(p) - i
s = ''
for i in range(l):
    s += '1'
print(int(s,2))
