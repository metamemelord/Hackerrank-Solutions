# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

n = int(input())
d = {}
vals = [int(x) for x in input().split()]
for i in range(len(vals)):
    if vals[i] in d:
        d[vals[i]].append(i)
    else:
        d[vals[i]] = []
        d[vals[i]].append(i)
mins = {}
for i in d:
    if len(d[i]) >= 2:
        for j in range(len(d[i])-1):
            d[i][j] = d[i][j+1] - d[i][j]
        mins[i] = min(d[i])
if len(mins) == 0:
    print(-1)
    quit()
print(min(list(mins.values())))
