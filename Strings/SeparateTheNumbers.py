# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:48:22 2017

@author: MetaMemeLord-
"""

def check(s):
    l = 1
    while l <= len(s)//2:
        k = s[:]
        val = int(s[:l])
        to_ret = val
        k = s[l:]
        while True:
            if len(k) == 0:
                return to_ret
            lel = str(val+1)
            val += 1
            if lel == k[:len(lel)]:
                k = k[len(lel):]
                continue
            break
        l += 1
    return -1
for _ in range(int(input())):
    s = input()
    val = check(s)
    if val == -1:
        print('NO')
    else:
        print('YES',val)
