# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

for _ in range(int(input())):
    n = int(input())
    x = [int(x) for x in input().split()]
    if n%2 == 0:
        print(0)
    else:
        ans = 0
        for i in range(0,len(x),2):
            ans ^= x[i]
        print(ans)
