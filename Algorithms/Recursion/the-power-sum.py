# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

import math

def candiv(x, n, i):
    val = x - math.pow(i,n)
    if(val < 0):
        return 0
    elif(val == 0):
        return 1
    else:
        return candiv(x,n,i+1) + candiv(val,n,i+1)

x = int(input())
n = int(input())
print(candiv(x,n,1))
