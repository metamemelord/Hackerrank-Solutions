# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 00:42:28 2017

@author: MetaMemeLord-
"""

def check(s):
    x = [ord(i) for i in s]
    l = 0
    r = len(x)-1
    while l<r:
        if abs(x[l]-x[l+1]) != abs(x[r]-x[r-1]):
            return 'Not Funny'
        l += 1
        r -= 1
    return 'Funny'

for _ in range(int(input())):
    s = input()
    print(check(s))
