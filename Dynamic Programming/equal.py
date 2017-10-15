# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

import sys

sys.setrecursionlimit(1000000000)
'''
def dp(x,operations):
    gap = x[len(x)-1] - x[0]
    if gap == 0:
        return operations
    if gap >= 5:
        x[len(x)-1] -= 5
        x.sort()
        return(dp(x,operations+1))
    elif gap>=2:
        x[len(x)-1] -= 2
        x.sort()
        return(dp(x,operations+1))
    else:
        x[len(x)-1] -= 1
        x.sort()
        return(dp(x,operations+1))
'''

for _ in range(int(input())):
    n = int(input())
    x = [int(i) for i in input().split()]
    x.sort()
    check = True
    min_sum,currentSum = float('inf'),0
    delta = [0,1,2,5]
    for i in range(len(delta)):
        currentSum = 0
        for j in range(1,len(x)):
            val = x[j] - x[0] + delta[i]
            currentSum += val//5 + ((val%5)//2) + ((val%5)%2)
        if min_sum > currentSum:
            if not check:
                min_sum = currentSum + 1
            else:
                min_sum = currentSum
        check = False
    print(min_sum)
