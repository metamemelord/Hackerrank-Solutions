# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
d ={chr(i+97):x for i, x in enumerate(input().split())}
word = input().strip()
n = []
for i in word:
    n.append(d[i])
print(int(max(n))*len(word))
