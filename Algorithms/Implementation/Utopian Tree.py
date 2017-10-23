# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

for _ in range(int(input())):
    c = int(input())
    k = c // 2
    m = 1 if c % 2 == 0 else 2
    print(2**(k+m) - m)
