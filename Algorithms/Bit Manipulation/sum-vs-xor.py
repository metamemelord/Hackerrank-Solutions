# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

x = int(input())
print(2**(bin(x).count('0')-1) if x else 1)
