# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
n, k = map(int, input().split())
x = n * k % 9
print(x if x!=0 else 9)
