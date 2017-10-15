# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

q = int(input())
for i in range(q):
    n = int(input())
    a = [int(x) for x in input().split()]
    max_sum = -100000000000000000000000000
    max_end = 0
    sum = 0
    for i in a:
        max_end += i
        if(max_sum<max_end):
            max_sum = max_end
        if(max_end < 0):
            max_end = 0
        if i>0:
            sum += i
    if max_sum<0:
        print(max_sum,max_sum)
    else:
        print(max_sum,sum)
