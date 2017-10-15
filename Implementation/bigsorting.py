# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

n = int(input().strip())
d = {}
for _ in range(n):
    number = input().strip()
    l = len(number)
    if not l in d:
        d[l] = []
    d[l].append(number)
for k in sorted(d):
    for val in sorted(d[k]):
        print(val)
