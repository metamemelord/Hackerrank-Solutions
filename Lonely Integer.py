# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

from functools import reduce

def lonelyinteger(a):
    # Complete this function
    return reduce((lambda x, y: x^y), a)
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
