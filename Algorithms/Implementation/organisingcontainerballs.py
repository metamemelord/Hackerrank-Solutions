# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

ans = []
for _ in range(int(input())):
    m = []
    sr = []
    sc = []
    check = True
    n = int(input())
    for __ in range(n):
        row = [int(x) for x in input().split()]
        m.append(row)
        sr.append(sum(row))
    for i in range(n):
        total   = 0
        for j in range(n):
            total += m[j][i]
        sc.append(total)
    sr.sort()
    sc.sort()
    if(sr==sc):
        print('Possible')
        continue
    print('Impossible')
